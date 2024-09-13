from django.shortcuts import render
from blog.models import Article


def home_page(request):
    articles = Article.objects.all()
    recent_articles = Article.objects.all().order_by('-updated', '-pub_date')[0:3]
    return render(request, 'home/index.html', {'articles': articles, 'recent_articles': recent_articles})
