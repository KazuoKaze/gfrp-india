from django.db import models

# Create your models here.

import uuid
from ckeditor.fields import RichTextField
from django.utils.text import slugify



from homePage.models import BaseModel


class HeroImage(BaseModel):
    image = models.ImageField(upload_to='about_hero/', blank=True, null=True) 

    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"image"

    class Meta:
        verbose_name_plural = 'About Hero Image'

class AboutHeroSection(BaseModel):
    title = models.CharField(max_length=2555, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ManyToManyField(HeroImage, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"About hero page {self.title or 'Untitled'}"

    class Meta:
        verbose_name_plural = 'About hero section'


class AboutOurStorySection(BaseModel):
    title = models.CharField(max_length=2555, blank=True, null=True)
    description = RichTextField()
    image = models.ImageField(upload_to='about_story/', blank=True, null=True) 
    
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Our story section {self.title or 'Untitled'}"

    class Meta:
        verbose_name_plural = 'Our story section'


class AboutValues(BaseModel):
    title = models.CharField(max_length=2555, blank=True, null=True)
    description = RichTextField()

    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Value section {self.title or 'Untitled'}"

    class Meta:
        verbose_name_plural = 'Value section'


class AboutSingleWhy(BaseModel):
    title = models.CharField(max_length=2555, blank=True, null=True)
    description = RichTextField()

    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Single why {self.title or 'Untitled'}"

    class Meta:
        verbose_name_plural = 'Single why'


class WholeWhySection(BaseModel):
    title = models.CharField(max_length=2555, blank=True, null=True)
    description = RichTextField()

    why = models.ManyToManyField(AboutSingleWhy, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Why section {self.title or 'Untitled'}"

    class Meta:
        verbose_name_plural = 'Why section'