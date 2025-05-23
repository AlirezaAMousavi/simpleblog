# Generated by Django 5.1 on 2024-08-30 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
