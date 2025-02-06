# локальный файл маршрута
from django.urls import path
from . import views  # . - указывает на текущую директорию

app_name = 'myportfolio_app'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
