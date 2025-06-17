from django.contrib import admin

# Register your models here.

# Register your models here.
from unfold.admin import ModelAdmin, TabularInline

from .models import Blog, Author, BlogPage
@admin.register(Author)
@admin.register(Blog)
@admin.register(BlogPage)

class CustomAdminClass(ModelAdmin):
    pass


