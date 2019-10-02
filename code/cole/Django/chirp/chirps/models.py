from django.db import models
from django.urls import reverse

# Create your models here.
class chirp(models.Model):
    username = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    chirpText = models.CharField(max_length=155)
    postDate = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.chirpText

    def get_absolute_url(self):
        return reverse('chirps:home', args=(self.id,))
