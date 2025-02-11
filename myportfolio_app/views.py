from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView
from .models import Project, Article
from django.contrib import messages


class HomeView(TemplateView):
    template_name = 'myportfolio_app/home.html'


class ProjectListView(ListView):
    model = Project
    template_name = 'myportfolio_app/projects.html'
    context_object_name = 'projects'
    paginate_by = 5


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'myportfolio_app/project_detail.html'
    context_object_name = 'project'

    def get_object(self):
        try:
            return super().get_object()
        except Project.DoesNotExist:
            messages.info(self.request, 'Нет проектов')
            return redirect('myportfolio_app/projects')


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'myportfolio_app/add_project.html'


class ArticleListView(ListView):
    model = Article
    template_name = 'myportfolio_app/articles.html'
    context_object_name = 'articles'
    paginate_by = 5


class ContactView(TemplateView):
    template_name = 'myportfolio_app/contact.html'
