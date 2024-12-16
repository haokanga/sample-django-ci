from django.test import TestCase
from .models import Item

class SimpleTestCase(TestCase):
    def test_passed_case(self):
        """This test is to demonstrate a passed test case."""
        self.assertEqual(len("hello"), 5, "This test is designed to pass for demonstration purposes.")

    def test_fix_this_failed_case(self):
        """This test is intentionally incorrect to demonstrate a failed test case for correction."""
        self.assertEqual(len("EASI"), 4, "This test is designed to fail for demonstration purposes.")