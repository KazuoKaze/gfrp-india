from django.db import models

# Create your models here.

import uuid
from ckeditor.fields import RichTextField
from django.utils.text import slugify

from homePage.models import BaseModel

class CarouselImage(BaseModel): 
    title = models.CharField(max_length=2555, blank=True, null=True)
    image = models.ImageField(upload_to='carousel_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CarouselImage {self.uuid}"

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"

class Application(BaseModel):
    title = models.CharField(max_length=2555, blank=True, null=True)
    image = models.ImageField(upload_to='application_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application {self.uuid} - {self.title}"

    class Meta:
        verbose_name = "Product Application"
        verbose_name_plural = "Product Applications"


class SingleProduct(BaseModel):
    title = models.CharField(max_length=2555, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    tag = models.CharField(max_length=2555, blank=True, null=True)
    application = models.ManyToManyField(Application, related_name='single_products', blank=True, null=True)
    image = models.ImageField(upload_to='single_product/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SingleProduct {self.uuid} - {self.title}"

    class Meta:
        verbose_name = "Single Product"
        verbose_name_plural = "Single Products"


class SingleProductSection(BaseModel):
    title = models.CharField(max_length=2555, blank=True, null=True)
    single_products = models.ManyToManyField(SingleProduct, related_name='single_product_sections', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SingleProductSection - {self.title}"

    class Meta:
        verbose_name = "Single Product Section"
        verbose_name_plural = "Single Product Sections"


class ProductPage(BaseModel):
    title = models.CharField(max_length=2555, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='product_page_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ProductPage - {self.title}"

    class Meta:
        verbose_name = "Product Page"
        verbose_name_plural = "Product Pages"