from django.test import TestCase
from .models import Item

class SimpleTestCase(TestCase):
    def test_passed_case(self):
        """This test is intentionally incorrect to demonstrate a failed test case for correction."""
        self.assertEqual(len("hello"), 5, "This test is designed to fail for demonstration purposes.")


