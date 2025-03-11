from django import forms
from .models import Project, Article, Contact


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'link']
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control", "placeholder": "Введите имя"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control", "placeholder": "Введите описание"
            })}


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'image']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        # widgets = {
        #     "name": forms.TextInput(attrs={
        #         "class": "form-control", "placeholder": "Введите имя"
        #     }),
        #     "email": forms.EmailInput(attrs={
        #         "class": "form-control", "placeholder": "Введите email"
        #     })} необходимо эту часть от-renderiть в html-шаблоне


class SearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=False, label="Поиск", widget=forms.TextInput(attrs={
        'placeholder': 'Поиск...',
        'class': 'form-control',
    }))