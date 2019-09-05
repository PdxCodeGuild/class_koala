from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    def __str__(self):
        return self.title
