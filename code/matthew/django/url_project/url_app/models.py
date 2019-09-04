from django.db import models
from django.utils import timezone

class UrlShortener(models.Model):
    code = models.CharField(max_length=6)
    long_url = models.CharField(max_length=400, null=True)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.code

class ClickData(models.Model):
    ip = models.CharField(max_length=45)
    time = models.DateTimeField(default = timezone.now)
    url = models.ForeignKey(UrlShortener, on_delete=models.CASCADE)

    def __str__(self):
        return self.ip