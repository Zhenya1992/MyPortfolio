from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class HomeView(View):

    def get(self, request):
        return HttpResponse("Главная страница")


class ProjectListView(View):

    def get(self, request):
        return HttpResponse("Страница проектов")


class ArticleListView(View):

    def get(self, request):
        return HttpResponse("Здесь находятся статьи")


class ContactView(View):

    def get(self, request):
        return HttpResponse("Контакты")
