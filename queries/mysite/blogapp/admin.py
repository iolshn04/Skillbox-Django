from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from .models import Article, Category, Tag, Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "bio"
    list_display_links = "pk", "name"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "pk", "name"
    list_display_links = "pk", "name"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = "pk", "name"
    list_display_links = "pk", "name"


class TagInline(admin.TabularInline):
    model = Article.tags.through

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        TagInline,
    ]
    list_display = "pk", "title", "content", "pub_date", "author", "category"
    list_display_links = "pk", "title"

    def get_queryset(self, request):
        return Article.objects.select_related("author").prefetch_related("tags")