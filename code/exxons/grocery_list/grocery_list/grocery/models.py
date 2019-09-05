from django.db import models
from django.utils import timezone
import datetime



class Item(models.Model):
    item_text = models.CharField(max_length=30)
    is_complete = models.BooleanField("complete", default=False)
    created_date = models.DateTimeField("created_date")
    
    def __str__(self):
        return self.item_text

    def complete_or_not(self):
        return self.is_complete


        