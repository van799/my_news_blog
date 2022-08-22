from django.core.paginator import Paginator
from django.shortcuts import render

from news.models import News


def index(request):

    news = News.objects.all()

    paginator = Paginator(news, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {'news_page': page_obj}

    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
