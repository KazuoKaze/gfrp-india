from django.contrib import admin

# Register your models here.
from unfold.admin import ModelAdmin, TabularInline

from .models import TechnicalResources, TechnicalResourceSection, ResourcesPage

@admin.register(TechnicalResourceSection)
@admin.register(TechnicalResources)

@admin.register(ResourcesPage)

class CustomAdminClass(ModelAdmin):
    pass
