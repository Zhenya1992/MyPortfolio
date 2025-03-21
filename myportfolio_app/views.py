from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
import traceback
from django.core.cache import cache
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView

from MyPortfolio import settings
from .forms import ContactForm, ProjectForm, ArticleForm, SearchForm
from .models import Project, Article
from django.contrib import messages
from django.core.mail import send_mail


class HomeView(TemplateView):
    template_name = 'myportfolio_app/home.html'


@method_decorator(cache_page(60 * 5), name="dispatch")
class ProjectListView(ListView):
    model = Project
    template_name = 'myportfolio_app/projects.html'
    context_object_name = 'projects'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("query", "")
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SearchForm(self.request.GET)
        return context


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'myportfolio_app/add_project.html'
    login_url = '/login/'

    def get_success_url(self):
        return reverse_lazy('myportfolio_app:projects')


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'myportfolio_app/project_detail.html'
    context_object_name = 'project'

    def get_object(self, queryset=None):

        pk = self.kwargs.get('pk')
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:

            messages.info(request, "На данный момент проектов нет.")
            return redirect('myportfolio_app:projects')
        return super().get(request, *args, **kwargs)


class ArticleListView(ListView):
    model = Article
    template_name = 'myportfolio_app/articles.html'
    context_object_name = 'articles'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("query", "")
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SearchForm(self.request.GET)
        return context


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'myportfolio_app/add_article.html'
    login_url = '/login/'

    def get_success_url(self):
        return reverse_lazy('myportfolio_app:articles')


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'myportfolio_app/article_detail.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):

        pk = self.kwargs.get('pk')
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:

            messages.info(request, "На данный момент статей нет.")
            return redirect('myportfolio_app:articles')
        return super().get(request, *args, **kwargs)


class ContactView(View):

    def get(self, request):
        form = ContactForm()
        return render(request, 'myportfolio_app/contact.html', {
            'form': form,
            'success': False,
            'spam_error': None,
        })

    def post(self, request):
        form = ContactForm(request.POST)

        if not SpamProtection.check_rate_limit(request):
            return render(request, "myportfolio_app/contact.html", {
                'form': None,
                'success': False,
                'spam_error': "Ты охерел, ты превысел лимит отправки сообщений. Свяжитись со мной:"
                              "<a href='https://t.me/Zecka92'>Telegram</a>."
            })

        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            try:
                send_mail(
                    subject=f"Сообщение от : {name}",
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
                return render(request, 'myportfolio_app/contact.html', {
                    'form': None,
                    'success': True,
                    'spam_error': None,
                })

            except Exception as e:
                error_trace = traceback.format_exc()
                print(error_trace, e)
                error_message = f"Ошибка при отправке : {e}"

            return render(request, 'myportfolio_app/contact.html', {
                'form': form,
                'success': False,
                'spam_error': error_message
            })
        return render(request, 'myportfolio_app/contact.html', {
            'form': form,
            'success': False,
            'spam_error': "Заполните форму повторно"
        })


class Custom404View(View):
    def get(self, request):
        return render(request, 'myportfolio_app/404.html', status=404)


def send_test_email(request):
    subject = "Тестовое сообщение"
    message = "Привет, проверка безопасности"
    from_email = 'zhenyagolenko92@gmail.com'
    recipient_list = ['ulia.maksimovich13@gmail.com']

    send_mail(subject, message, from_email, recipient_list)
    return HttpResponse("Письмо отправлено")


class SpamProtection:

    @staticmethod
    def check_rate_limit(request):
        user_ip = request.META.get("REMOTE_ADDR")
        cache_key = f"Rate_limit: {user_ip}"
        requests_count = cache.get(cache_key, 0)

        if requests_count >= 2:
            return False
        if requests_count == 0:
            cache.set(cache_key, 1, timeout=60)
        else:
            cache.incr(cache_key, 1)
        return True
