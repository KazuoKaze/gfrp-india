from django.contrib import admin

# Register your models here.
from unfold.admin import ModelAdmin, TabularInline

from .models import ContactPage

@admin.register(ContactPage)

class CustomAdminClass(ModelAdmin):
    pass
