from django.contrib import admin
from .models import Project, Article, Contact

admin.site.site_header = "Мой проект"
admin.site.site_title = "Проект Евгена"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "link", "created_at")
    search_fields = ("title",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "image", "created_at")
    search_fields = ("title",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message", "created_at")
    search_fields = ("name",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)
