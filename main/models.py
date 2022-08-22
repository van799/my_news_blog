from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class IndexNews(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now=True)
    text = models.TextField('Текст заглавной странице')
    image = models.ImageField(
        'Картинка',
        upload_to='main/',
        blank=True)
