from django.contrib import admin
from .models import UrlShortener, ClickData

admin.site.register(UrlShortener)
admin.site.register(ClickData)
