from django.contrib import admin

# Register your models here.

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'create', 'publish', 'author']
    search_fields = ['title', 'desc']
    prepopulated_fields = {'slug': ('title', 'author')}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
