from django.forms import ModelForm, TextInput, Textarea

from .models import News


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'anons', 'text', 'image']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название новости'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс новости'
            }),

            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'текст новости'
            }),


        }
