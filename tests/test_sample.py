from unittest import TestCase

from src import my_module


class MyTest(TestCase):
    def test(self):
        result = my_module.addOne(1)
        self.assertEqual(result, 3)
