from django.db import models
from django.urls import reverse

class Chirp(models.Model):
    username = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    body = models.CharField(max_length=140)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
    
    def get_absolute_url(self):
        return reverse('chirps:detail', args=(self.id,))