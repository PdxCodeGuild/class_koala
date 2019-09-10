from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class URL(models.Model):
    longURL = models.CharField(max_length=500)
    urlcode = models.CharField(max_length=6, default = '')
    shortURL = models.CharField(max_length=20, default = '')
    createdTime = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return self.shortURL

    def get_absolute_url(self):
        return reverse('URLShortener:index')
