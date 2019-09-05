import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import GroceryItem

def create_item(item_text):
    return GroceryItem.objects.create(item_text=item_text)

class QuestionIndexViewTests(TestCase):

    def test_no_groceries(self):
        """
        checks premise of an empty grocery list and passes if page loads successfully and an empty list is returned
        """
        response = self.client.get(reverse('grocery_app:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['grocery_items'], [])

    def test_one_grocery_item(self):
        """
        checks premise of a grocery list with only one item and passes if only one item is returned
        """
        create_item(item_text='Grocery item.')
        response = self.client.get(reverse('grocery_app:index'))
        self.assertQuerysetEqual(
            response.context['grocery_items'], ['<GroceryItem: Grocery item.>']
        )

    def test_two_grocery_items(self):
        """
        checks premise of a grocery list with more than one item and passes if more than one item is returned
        """
        create_item(item_text='Grocery item 1.')
        create_item(item_text='Grocery item 2.')
        response = self.client.get(reverse('grocery_app:index'))
        self.assertQuerysetEqual(
            response.context['grocery_items'],
            ['<GroceryItem: Grocery item 2.>',
            '<GroceryItem: Grocery item 1.>'], ordered=False
        )