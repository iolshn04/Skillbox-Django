# Generated by Django 4.1.6 on 2023-09-06 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_category_tag_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='articles', to='blogapp.tag'),
        ),
    ]