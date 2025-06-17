from django.urls import path
from .views import single_product_section_view, product_page_view

urlpatterns = [
    path('single_product_section/', single_product_section_view, name='single_product_section_view'),
    path('product_page/', product_page_view, name='product_page_view'),
]