from django.contrib import admin
from .models import Post


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin interface for Post model."""
    listDisplay = ('title', 'author', 'created_at', 'updated_at')
    searchFields = ('title', 'body')
    listFilter = ('author', 'updated_at')
    prepopulatedFields = {'slug': ('title',)}
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'