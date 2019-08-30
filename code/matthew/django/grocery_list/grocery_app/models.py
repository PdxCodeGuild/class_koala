import datetime

from django.db import models
from django.utils import timezone

class GroceryItem(models.Model):
    item_text = models.CharField(max_length=200)
    created_date = models.DateTimeField("date created", default=timezone.now())
    completed_date = models.DateTimeField("date completed", default=timezone.now())
    is_item_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item_text
    
