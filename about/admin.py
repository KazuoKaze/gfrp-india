from django.contrib import admin

# Register your models here.
from .models import HeroImage, AboutHeroSection, AboutOurStorySection, AboutSingleWhy, AboutValues, WholeWhySection

from unfold.admin import ModelAdmin, TabularInline

@admin.register(HeroImage)
@admin.register(AboutHeroSection)
@admin.register(AboutOurStorySection)
@admin.register(AboutSingleWhy)
@admin.register(AboutValues)
@admin.register(WholeWhySection)

class CustomAdminClass(ModelAdmin):
    pass