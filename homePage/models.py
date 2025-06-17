from django.db import models

# Create your models here.

import uuid
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.

class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True


class HeroSection(BaseModel):
    small_title = models.CharField(max_length=2555, blank=True, null=True)
    title = models.CharField(max_length=2555, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='hero_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"HeroSection {self.uuid} - {self.title}"
    
    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Sections"


class AboutSection(BaseModel):
    testimonial_title = models.CharField(max_length=2555, blank=True, null=True)
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='about_images/', blank=True, null=True)
    title = models.CharField(max_length=2555, blank=True, null=True)
    description = RichTextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AboutSection {self.uuid} - {self.title}"

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Sections"


class SubSectionOfHowToStart(BaseModel):
    title = models.CharField(max_length=2555, blank=True, null=True)
    description = RichTextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SubSectionOfHowToStart {self.uuid} - {self.title}"

    class Meta:
        verbose_name = "Sub Section of How To Start"
        verbose_name_plural = "Sub Sections of How To Start"


class HowToStartSection(BaseModel):
    title = models.CharField(max_length=2555, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='how_to_start_images/', blank=True, null=True)
    sub_sections = models.ManyToManyField(SubSectionOfHowToStart, related_name='how_to_start_sections', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"HowToStartSection {self.uuid} - {self.title}"

    class Meta:
        verbose_name = "How To Start Section"
        verbose_name_plural = "How To Start Sections"


class SingleProduction(BaseModel):
    title = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SingleProduction {self.uuid} - {self.title}"

    class Meta:
        verbose_name = "Product info"
        verbose_name_plural = "Product infos"


class SingleProductionSection(BaseModel):
    title = RichTextField(max_length=2555, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='production_images/', blank=True, null=True)

    single_production = models.ManyToManyField(SingleProduction, related_name='sections')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SingleProductionSection {self.uuid} - {self.title}"

    class Meta:
        verbose_name = "Single Product info"
        verbose_name_plural = "Single Product infos"


class ProductionSection(BaseModel):
    title = models.CharField(max_length=2555, blank=True, null=True)
    production = models.ManyToManyField(SingleProductionSection, related_name='production_sections')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ProductionSection {self.uuid} - {self.title}"

    class Meta:
        verbose_name = "Whole Production Section"
        verbose_name_plural = "Whole Production Sections"


