from django.urls import path
from .views import get_contact, contact_form_view

urlpatterns = [
    path('get_contact/', get_contact, name='get_contact'),
    path('contact_form_view/', contact_form_view, name='contact_form_view'),
]