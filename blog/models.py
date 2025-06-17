from django.db import models

# Create your models here.

import uuid
from ckeditor.fields import RichTextField
from django.utils.text import slugify



from homePage.models import BaseModel


class Author(BaseModel):
    name = models.CharField(max_length=2555)
    profile_picture = models.ImageField(upload_to='authors/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Authors'


class Blog(BaseModel):
    tag = models.CharField(max_length=2555)
    min_read = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=2555)
    slug = models.SlugField(unique=True, blank=True, max_length=2555)
    description = models.TextField()

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blogs', blank=True, null=True)
   
    is_published = models.BooleanField(default=False)
    content = RichTextField()
    related_blogs = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            raw_slug = slugify(self.title)
            if len(raw_slug) > 2555:
                # Cut at the last dash before 255 chars
                raw_slug = raw_slug[:2555]
                last_dash = raw_slug.rfind('-')
                if last_dash > 0:
                    raw_slug = raw_slug[:last_dash]
            self.slug = raw_slug
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Blogs'


class BlogPage(BaseModel):
    title = models.CharField(max_length=2555, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='blog_page/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Blog page {self.title or 'Untitled'}"

    class Meta:
        verbose_name_plural = 'Blog Page'