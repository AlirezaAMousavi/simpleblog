from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category, Comment, ContactUs
from .forms import ContactUsForm
from django.core.paginator import Paginator
from django.contrib import messages


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    num_comments = len(article.comments.all())
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        content = request.POST.get('content')
        if parent_id:
            Comment.objects.create(content=content, article=article, author=request.user, parent_id=int(parent_id))
        else:
            Comment.objects.create(content=content, article=article, author=request.user)
        return redirect('blog:article_detail', slug=slug)
    return render(request, 'blog/article_details.html',
                  {'article': article, 'num_comments': num_comments})


def article_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(object_list=articles, per_page=1)
    objects_list = paginator.get_page(page_number)
    return render(request, 'blog/articles_list.html', {'articles': objects_list})


def search_form(request):
    search = request.GET.get('search')
    articles = Article.objects.filter(title__icontains=search)
    page_number = request.GET.get('page')
    paginator = Paginator(object_list=articles, per_page=1)
    objects_list = paginator.get_page(page_number)
    return render(request, 'blog/articles_list.html', {'articles': objects_list})


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    articles = category.articles.all()
    return render(request, 'blog/articles_list.html', {'articles': articles})


def contact_form(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:contact_form')
    else:
        form = ContactUsForm()
    return render(request, "blog/contact_us.html", {'form': form})