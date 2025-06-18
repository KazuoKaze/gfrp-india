from django.urls import path
from .views import get_about_hero, get_about_story, get_value, get_why

urlpatterns = [
    path('get_about_hero/', get_about_hero, name='get_about_hero'),
    path('get_about_story/', get_about_story, name='get_about_story'),
    path('get_value/', get_value, name='get_value'),
    path('get_why/', get_why, name='get_why'),
]