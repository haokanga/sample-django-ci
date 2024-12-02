from django.test import TestCase
from .models import Item

class SimpleTestCase(TestCase):
    def test_passed_case(self):
        """This test is to demonstrate a passed test case."""
        self.assertEqual(len("hello"), 5, "This test is designed to pass for demonstration purposes.")
