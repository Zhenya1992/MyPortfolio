# локальный файл маршрута
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views  # . - указывает на текущую директорию
from . import api_views

app_name = 'myportfolio_app'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('add_project/', views.ProjectCreateView.as_view(), name='add_project'),
    path('add_article/', views.ArticleCreateView.as_view(), name='add_article'),
    path('articles/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('404/', views.Custom404View.as_view(), name='custom404'),
    path('send_mail/', views.send_test_email, name='send_test_mail'),
    path('api/projects', api_views.ProjectListApi.as_view(), name='api_projects'),
    path('api/articles', api_views.ArticleListApi.as_view(), name='api_articles'),
    path('api/projects_detail/<int:pk>/', api_views.ProjectDetailApi.as_view(), name='api_projects_detail'),
    path('api/articles_detail/<int:pk>/', api_views.ArticleDetailApi.as_view(), name='api_articles_detail'),
    path('api/add_article/', api_views.ArticleCreateApi.as_view(), name='api_add_article'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
