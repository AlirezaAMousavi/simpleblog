from blog.models import Article, Category


def recent_articles_side_bar(request):
    recent_articles_sidebar = Article.objects.order_by('-updated', '-pub_date')[0:3]
    return {'recent_articles_sidebar': recent_articles_sidebar}

def category_side_bar(request):
    category_sidebar = Category.objects.all()
    return {'category_sidebar': category_sidebar}