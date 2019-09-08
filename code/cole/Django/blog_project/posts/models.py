from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    body = models.CharField(max_length=10000)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', args={self.id,})
