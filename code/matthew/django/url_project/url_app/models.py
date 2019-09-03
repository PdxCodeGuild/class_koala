from django.db import models

class UrlShortener(models.Model):
    code = models.CharField(max_length=6)
    long_url = models.CharField(max_length=400, null=True)

    def __str__(self):
        return self.code