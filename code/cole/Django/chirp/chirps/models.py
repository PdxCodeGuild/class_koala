from django.db import models
from django.utils import timezone
# Create your models here.
class chirp(models.Model):
    chirpText = models.CharField(max_length=500)
    postDate = models.DateTimeField(default = timezone.now())
    chirpAuth = models.CharField(max_length = 50)
