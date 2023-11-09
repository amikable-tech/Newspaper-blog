from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class Category(models.Model):
    name = models.CharField('Name', max_length=100, blank=False)

    tags = TaggableManager()