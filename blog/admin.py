from django.contrib import admin
from .models import Article

# Register your models here.
# admin.site.register(Article)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'published', 'status']
    list_filter = ['status', 'created', 'published', 'author']
    search_fields = ['title', 'body']
    pass

