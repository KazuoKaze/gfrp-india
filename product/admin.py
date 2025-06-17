from django.contrib import admin

# Register your models here.
from unfold.admin import ModelAdmin, TabularInline

from .models import CarouselImage, Application, SingleProduct, SingleProductSection, ProductPage

@admin.register(CarouselImage)
@admin.register(Application)
@admin.register(SingleProduct)
@admin.register(SingleProductSection)
@admin.register(ProductPage)

class CustomAdminClass(ModelAdmin):
    pass
