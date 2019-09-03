from django.test import TestCase
from django.urls import reverse

from .models import UrlShortener

class UrlShortenerIndexViewTests(TestCase):

    def test_successful_load(self):
        response = self.client.get(reverse("url_app:index"))
        self.assertEqual(response.status_code, 200)