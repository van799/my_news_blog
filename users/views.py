from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.form import CreationForm


app_name = 'users'


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('my_news')
    template_name = 'users/signup.html'
