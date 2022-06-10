"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
<<<<<<< HEAD
        """Test for subtracting numbers."""
=======
        """Test subtracting numbers."""
>>>>>>> 9c48f62c5a68919b04a906b7b0ac6292c23264d1
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
