from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView
from .models import Project, Article


class HomeView(TemplateView):
    template_name = 'myportfolio_app/home.html'


class ProjectListView(ListView):
    model = Project
    template_name = 'myportfolio_app/projects.html'
    context_object_name = 'projects'
    paginate_by = 5


class ArticleListView(ListView):
    model = Article
    template_name = 'myportfolio_app/articles.html'
    context_object_name = 'articles'
    paginate_by = 5


class ContactView(View):

    def get(self, request):
        return HttpResponse("Контакты")
