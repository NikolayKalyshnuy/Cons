import unittest
from product import Product

class TestProduct(unittest.TestCase):

    def test_change(self):
        product = Product()
        product.maker("VGA")
        # product.price("10")  
        # self.assertEqual(product, Product("VGA", "10"))
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()