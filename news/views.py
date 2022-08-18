from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView

from .forms import NewsForm
from .models import News


def my_news(request):
    news = News.objects.all().order_by('-data')
    paginator = Paginator(news, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {'news_page': page_obj}
    return render(request, 'news/news_home.html', data)


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'news/create.html'
    form_class = NewsForm


class NewsDeleteView(DeleteView):
    model = News
    success_url = '/news'
    template_name = 'news/news_delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('my_news')
        else:
            error = "Форма заполнена не верно"
    form = NewsForm
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'news/create.html', data)
