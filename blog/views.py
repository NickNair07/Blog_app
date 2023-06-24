from django.shortcuts import render, get_object_or_404
from .models import Article
from django.http import Http404, HttpResponse

# Create your views here.
def list_of_articles(request):
    articles = Article.publishedArticles.all()
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
