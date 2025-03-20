from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import ProjectSerializer, ArticleSerializer
from .models import Project, Article


class ProjectListApi(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

    filter_backends = [SearchFilter, OrderingFilter]

    search_fields = ["title", "description"]
    ordering_fields = ["title", "description"]
    ordering = ["created_at"]


class ArticleListApi(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]

    filter_backends = [SearchFilter, OrderingFilter]

    search_fields = ["title", "description"]
    ordering_fields = ["title", "description"]
    ordering = ["created_at"]


class ProjectDetailApi(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]


class ArticleDetailApi(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]


class ArticleCreateApi(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
