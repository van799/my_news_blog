from django import forms

from .models import IndexNews


class MainForm(forms.IndexNews):
    class Meta:
        model = IndexNews
        fields = ['title', 'data', 'text', 'image']
