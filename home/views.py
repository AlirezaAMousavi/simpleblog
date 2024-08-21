from django.shortcuts import render
from blog.models import Article

def home_page(request):
    articles = Article.objects.all()
    return render(request, 'home/index.html', {'articles': articles})
