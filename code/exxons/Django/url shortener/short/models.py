from django.db import models
from django.utils.text import slugify 

class URL(models.Model):
    url_text = models.TextField()
    pub_date = models.DateTimeField("date published")
    short_code = models.SlugField(max_length=6)

    def __str__(self):
        return self.url_text


