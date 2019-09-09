from django.db import models
from django.urls import reverse

class GroceryItem(models.Model):
    itemText = models.CharField(max_length=200)
    itemCount = models.IntegerField()
    createdDate = models.DateTimeField()
    completedDate = models.DateTimeField(default = '')
    completed = models.BooleanField(default = False)

    def __str__(self):
        return self.itemText

    def get_absolute_url(self):
        return reverse('GroceryList:list')
