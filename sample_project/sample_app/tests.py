from django.test import TestCase
from .models import Item

class SimpleTestCase(TestCase):
    def test_passing_math(self):
        """Test that basic math works (2 + 2 = 4)."""
        self.assertEqual(2 + 2, 4, "Math is broken: 2 + 2 should equal 4.")

    def test_string_equality(self):
        """Test that two strings are equal."""
        self.assertEqual("hello", "hello", "The strings 'hello' and 'hello' should be equal.")

