from django.core.management import BaseCommand

from django.db import transaction

from blogapp.models import Article, Author, Tag, Category

class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write("Create articles with tags")
        author = Author.objects.get(name='Андрей')
        category = Category.objects.get(pk='1')
        tags = Tag.objects.all()
        article, created = Article.objects.get_or_create(
            title="Новые истории",
            author=author,
            category=category,
        )
        for tag in tags:
            article.tags.add(tag)
        article.save()
        self.stdout.write(f"Created article {article}")