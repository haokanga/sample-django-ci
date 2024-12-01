from django.test import TestCase
from .models import Item

class ItemTestCase(TestCase):
    def setUp(self):
        Item.objects.create(name="Test Item")

    def test_item_creation(self):
        item = Item.objects.get(name="Test Item")
        self.assertEqual(item.name, "Test Item")
