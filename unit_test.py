from unittest import TestCase
from test_class import TestClass


class UnitTest(TestCase):

    def test_add(self):
        tc = TestClass()
        first = tc.add(10, 1)
        second = 11
        self.assertEqual(first, second)

    def test_subtract(self):
        tc = TestClass()
        first = tc.subtract(10, 1)
        second = 9
        self.assertEqual(first, second)

    def test_multiply(self):
        tc = TestClass()
        first = tc.multiply(5, 2)
        second = 10
        self.assertEqual(first, second)

    def test_divide(self):
        tc = TestClass()
        first = tc.divide(10, 2)
        second = 5
        self.assertEqual(first, second)
