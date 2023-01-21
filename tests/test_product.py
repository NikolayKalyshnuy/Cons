import unittest
from product import Product, format

class TestProduct(unittest.TestCase):

    def test_format(self):
        res = format("\r\nfsf fdhg\n   \r  ")
        self.assertEqual(res, "fsf fdhg")

    def test_change(self):
        car = Product()
        car.maker = "VGA"
        car.price = "10"
        self.assertEqual(car, Product("VGA", "10"))

if __name__ == '__main__':
    unittest.main()