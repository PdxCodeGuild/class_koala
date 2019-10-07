from django.db import models
from django.urls import reverse

class Posts(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"pk": self.id})
    