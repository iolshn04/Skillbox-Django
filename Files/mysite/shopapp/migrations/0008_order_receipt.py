# Generated by Django 4.0.6 on 2023-08-29 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0007_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='receipt',
            field=models.FileField(null=True, upload_to='orders/receipts/'),
        ),
    ]
