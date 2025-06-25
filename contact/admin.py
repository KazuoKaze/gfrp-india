from django.contrib import admin

# Register your models here.
from unfold.admin import ModelAdmin, TabularInline

from .models import ContactPage, ContactForm

@admin.register(ContactPage)
@admin.register(ContactForm)

class CustomAdminClass(ModelAdmin):
    pass
