from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Article
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "articles/create_article.html"
    fields = ("title", "body",)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "articles/article_list.html"
    context_object_name = "articles"
    queryset = Article.objects.all().order_by("-date")

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "articles/article_detail.html"
    context_object_name = "article"

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = "articles/article_edit.html"
    fields = ('title', 'body')

    def test_func(self, *args, **kwargs):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "articles/article_delete.html"
    success_url = reverse_lazy('article_list')
    context_data_name = "article"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


