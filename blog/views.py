from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Comment
from django.core.paginator import Paginator
from accounts.models import Profile


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    num_comments = len(article.comments.all())
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(content=content, article=article, author=request.user)

    return render(request, 'blog/article_details.html',
                  {'article': article, 'profile': profile, 'num_comments': num_comments})


def article_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(object_list=articles, per_page=1)
    objects_list = paginator.get_page(page_number)
    return render(request, 'blog/articles_list.html', {'articles': objects_list})


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    articles = category.articles.all()
    return render(request, 'blog/articles_list.html', {'articles': articles})
