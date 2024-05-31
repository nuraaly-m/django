from django.db import models

# Create your models here.

class TagCloth(models.Model):
    name = models.CharField(max_length=100)

class Cloth(models.Model):
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=500)
    tags = models.ManyToManyField(TagCloth)
