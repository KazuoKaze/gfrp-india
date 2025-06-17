from django.db import models

# Create your models here.


import uuid
from ckeditor.fields import RichTextField
from django.utils.text import slugify



from homePage.models import BaseModel


class TechnicalResources(BaseModel):
    title = models.CharField(max_length=2555, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    file = models.FileField(upload_to='technical_resources_files/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"TechnicalResource {self.uuid} - {self.title}"

    class Meta:
        verbose_name = "Technical Resource"
        verbose_name_plural = "Technical Resources"


class TechnicalResourceSection(BaseModel):
    title = models.CharField(max_length=2555, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    technical_resources = models.ManyToManyField(TechnicalResources, related_name='technical_resource_sections', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"TechnicalResourceSection {self.uuid} - {self.title}"

    class Meta:
        verbose_name = "Technical Resource Section"
        verbose_name_plural = "Technical Resource Sections"


class ResourcesPage(BaseModel):
    title = models.CharField(max_length=2555, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='resources_page/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ResourcesPage {self.uuid} - {self.title}"

    class Meta:
        verbose_name = "Resources Page"
        verbose_name_plural = "Resources Pages"