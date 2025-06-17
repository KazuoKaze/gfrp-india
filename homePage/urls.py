from .views import hero_section_list, about_section_list, how_to_start_section_list, production_section_list
from django.urls import path

urlpatterns = [
    path('hero_section/', hero_section_list, name='hero_section_list'),
    path('about_section/', about_section_list, name='about_section_list'),
    path('how_to_start_section/', how_to_start_section_list, name='how_to_start_section_list'),
    path('production_section/', production_section_list, name='production_section_list'),
]