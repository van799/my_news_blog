from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class News(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=255)
    text = models.TextField('Текст новости')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    data = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        ordering = ('-data',)
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
