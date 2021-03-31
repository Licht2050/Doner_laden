from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class ResourceCatagory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = 'Catagories'

    def __str__(self):
        return self.name

class ResourceProduct(models.Model):
    catagory = models.ManyToManyField(ResourceCatagory)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(blank=True)
    quantity = models.FloatField()

    def __str__(self):
        return self.name