from django.db import models
from .choices import NEIGHBORHOODS

class Cart(models.Model):
    name = models.CharField(max_length = 50)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length = 12, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    twitter = models.CharField(max_length = 15, blank=True)
    instagram = models.CharField(max_length = 30, blank=True)
    facebook = models.CharField(max_length = 50, blank=True)
    image = models.ImageField(blank=True)
    neighborhood = models.CharField(max_length = 50, choices = NEIGHBORHOODS)
    cuisines = models.ManyToManyField("Cuisine")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Cuisine(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name