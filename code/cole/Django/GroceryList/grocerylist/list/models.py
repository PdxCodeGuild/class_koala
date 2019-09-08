from django.db import models

class GroceryItem(models.Model):
    itemText = models.CharField(max_length=200)
    itemCount = models.IntegerField()
    createdDate = models.DateTimeField()
    completedDate = models.DateTimeField(default = '')
    completed = False

    def __str__(self):
        return self.itemText
