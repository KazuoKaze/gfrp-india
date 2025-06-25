from django.contrib import admin

# Register your models here.
from unfold.admin import ModelAdmin, TabularInline

from .models import HeroSection, AboutSection, SubSectionOfHowToStart, HowToStartSection, SingleProductionSection, SingleProduction, ProductionSection, FAQSection, NewsLetter

# @admin.register(AboutSection)

# @admin.register(HeroSection)

# @admin.register(SubSectionOfHowToStart)

# @admin.register(HowToStartSection)

# @admin.register(SingleProductionSection)
# @admin.register(SingleProduction)
# @admin.register(ProductionSection)

# class CustomAdminClass(ModelAdmin):
#     pass



@admin.register(HeroSection)
class HeroSectionAdmin(ModelAdmin):
    show_in_sidebar = False

@admin.register(AboutSection)
class AboutSectionAdmin(ModelAdmin):
    show_in_sidebar = False

@admin.register(HowToStartSection)
class HowToStartSectionAdmin(ModelAdmin):
    show_in_sidebar = False

@admin.register(SubSectionOfHowToStart)
class SubSectionOfHowToStartAdmin(ModelAdmin):
    show_in_sidebar = False

@admin.register(SingleProduction)
class SingleProductionAdmin(ModelAdmin):
    show_in_sidebar = False

@admin.register(SingleProductionSection)
class SingleProductionSectionAdmin(ModelAdmin):
    show_in_sidebar = False

@admin.register(ProductionSection)
class ProductionSectionAdmin(ModelAdmin):
    show_in_sidebar = False

@admin.register(FAQSection)
class FAQSectionAdmin(ModelAdmin):
    show_in_sidebar = False

@admin.register(NewsLetter)
class NewsletterSectionAdmin(ModelAdmin):
    show_in_sidebar = False