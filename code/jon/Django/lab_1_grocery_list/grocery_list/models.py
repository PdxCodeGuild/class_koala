import datetime

from django.db import models
from django.utils import timezone

class GroceryItem(models.Model):
    grocery_text = models.CharField(max_length=200)
    created_date = models.DateTimeField('Date Listed')
    is_complete = models.BooleanField

    def __str__(self):
        return self.grocery_text

    def created_date(self):
        return self.timezone.now()