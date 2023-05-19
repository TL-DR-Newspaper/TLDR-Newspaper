from django.db import models
from newssources.models import Source
from datetime import datetime
from django.utils.text import slugify


# Create your models here.
class Article(models.Model):
    pubdate = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=500)
    imageurl = models.URLField(blank=True,max_length=5000)
    summary = models.TextField(blank=True, null=True, max_length=50000)
    comparison = models.TextField(max_length=50000)
    sources = models.ManyToManyField(Source)
    slug = models.SlugField(blank=True, max_length=500)
    published = models.BooleanField(default=False)
    created_by_ai = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})  

    
class Test(models.Model):
    sources = models.ManyToManyField(Source)
