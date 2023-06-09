from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    class ArticlePublishedManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=Article.Status.PUBLISHED)
            pass
        pass

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_articles')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='published')
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager() #The default manager
    publishedArticles = ArticlePublishedManager() #The custom manager

    class Meta:
        # To add the descending order by published_date
        ordering = ['-published']

        # To define an index with a descending order for a column
        indexes = [
            models.Index(fields=['-published'])
        ]

    def __str__(self):
        return self.title
        pass
    # For SEO Friendly URLs 
    def get_canonical_url(self):
        return reverse('blog:article_details', 
                        args=[
                                self.published.year,
                                self.published.month,
                                self.published.day,
                                self.slug
                            ]
                        )
        pass
    pass
    