import unittest
from testing import calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = calculator.add(10, 5)
        self.assertEqual(result, 15)

    def test_subtract(self):
        result = calculator.sub(7, 2)       # If you want to test an assertion multiple times, best practice to replace the numbers in a seperate line
        self.assertEqual(result, 5)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)

        self.assertRaises(ValueError, calculator.divide, 10, 0)         # This allows the test to pass as we have set up a ValueError
