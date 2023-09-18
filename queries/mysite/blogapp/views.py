from django.shortcuts import render
from django.views.generic import ListView

from blogapp.models import Article


class ArticlesListView(ListView):
    template_name = "blogapp/article_list.html"
    context_object_name = "articles"
    queryset = Article.objects.select_related('author').prefetch_related('tags')
