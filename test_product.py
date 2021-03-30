import unittest
from product import get_product


class TestGetProduct(unittest.TestCase):
    def test_product(self):
        self.assertEqual(get_product(2, 3), 2*3)

    def test_type_error(self):
        self.assertRaises(TypeError, get_product, '2', '3')
        self.assertRaises(TypeError, get_product, True, False)
