from django.contrib import admin
from .models import Article

# Register your models here.
# admin.site.register(Article)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'published_at', 'status']
    list_filter = ['status', 'created_at', 'published_at', 'author']
    search_fields = ['title', 'body']
    pass

