from django.db import models

# Create your models here.

import uuid
from ckeditor.fields import RichTextField
from django.utils.text import slugify



from homePage.models import BaseModel


class ContactPage(BaseModel):
    title = models.CharField(max_length=2555, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='contact_page/', blank=True, null=True)

    phone = models.CharField(max_length=2555, blank=True, null=True)
    email_address = models.EmailField()
    address = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Contact page {self.title or 'Untitled'}"

    class Meta:
        verbose_name_plural = 'Contact Page'




class ContactForm(BaseModel):
    first_name = models.CharField(max_length=2555, blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)

    phone = models.CharField(max_length=2555, blank=True, null=True)
    email_address = models.EmailField()
    machine = models.CharField(max_length=2555, blank=True, null=True)
    message = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.first_name or 'Untitled'}"

    class Meta:
        verbose_name_plural = 'Contact Form'