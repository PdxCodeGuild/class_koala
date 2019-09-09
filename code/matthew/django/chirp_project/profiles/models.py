from django.db import models

class Profile(models.Model):
    username = models.OneToOneField('auth.User', on_delete = models.CASCADE)
    displayname = models.CharField(max_length = 50)

    def __str__(self):
        return self.displayname