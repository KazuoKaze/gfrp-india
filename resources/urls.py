from django.urls import path
from .views import technical_resource_section_view, technical_resources_view

urlpatterns = [
    path('technical_resource_section/', technical_resource_section_view, name='technical_resource_section_view'),
    path('technical_resources/', technical_resources_view, name='technical_resources_view'),
]

