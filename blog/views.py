from django.shortcuts import render, get_object_or_404
from .models import Article
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def list_of_articles(request):
    articles = Article.publishedArticles.all()
    paginator = Paginator(articles, 1)
    page_number = request.GET.get('page', 1)
    try:
        articles = paginator.page(page_number)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        articles = paginator.page(1)

    return render(request, 'blog/list.html', {'articles': articles})


def article_details(request, year, month, day, article):
    try:
        article = get_object_or_404(Article, status=Article.Status.PUBLISHED, 
                    slug=article,
                    published__year=year,
                    published__month=month,
                    published__day=day
                )
    except Article.DoesNotExist:
        raise Http404("No article found.")
    
    return render(request, 'blog/detail.html', {'article': article})
    pass
