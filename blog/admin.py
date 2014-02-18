from django.contrib import admin
from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['title', 'description']
    # fields to filter the change list with
    list_filter = ['categories', 'published', 'created']
    # fields to search in change list
    search_fields = ['title', 'description', 'content']
    # enable the date drill down on change list
    date_hierarchy = 'created'
    # prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
