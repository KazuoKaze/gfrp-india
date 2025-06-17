from django.urls import path
from .views import blog_home_list_view, blog_page_view, blog_detail_view

urlpatterns = [
    path('blog_home_list/', blog_home_list_view, name='blog_home_list_view'),
    path('blog_page/', blog_page_view, name='blog_page_view'),
    path('blog_detail/<slug:slug>/', blog_detail_view, name='blog_detail_view'),
]