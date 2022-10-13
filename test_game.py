from unittest import TestCase, TextTestRunner, TestSuite, TestLoader, main

class MyTests2(TestCase):
    def test_one(self):
        self.assertEqual(1, 1)