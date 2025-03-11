from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="проект")
    description = models.TextField(verbose_name="описание")
    link = models.URLField(blank=True, null=True, verbose_name="ссылка")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")

    class Meta:
        verbose_name = "мои проект"
        verbose_name_plural = "мои проекты"

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="название")
    description = models.TextField(verbose_name="описание")
    image = models.ImageField(upload_to='articles/', blank=True, null=True, verbose_name='изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    email = models.EmailField(verbose_name="email")
    message = models.TextField(verbose_name="сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")

    class Meta:
        verbose_name = "контакт"
        verbose_name_plural = "контакты"

    def __str__(self):
        return f"Сообщение от : {self.name}"
