from django.contrib import admin

# Register your models here.
from unfold.admin import ModelAdmin, TabularInline

from .models import HeroSection, AboutSection, SubSectionOfHowToStart, HowToStartSection, SingleProductionSection, SingleProduction, ProductionSection

@admin.register(AboutSection)

@admin.register(HeroSection)

@admin.register(SubSectionOfHowToStart)

@admin.register(HowToStartSection)

@admin.register(SingleProductionSection)
@admin.register(SingleProduction)
@admin.register(ProductionSection)

class CustomAdminClass(ModelAdmin):
    pass
