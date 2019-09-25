from django.db import models

class StartingURL (models.Model):
    longurl = models.CharField(max_length=100)
    code = models.CharField(max_length=6)

    def __str__(self):
        return self.longurl