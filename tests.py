# testing code for surfshop
import surfshop
import unittest
import datetime


class TestSurfShop(unittest.TestCase):
    def setUp(self):
        self.cart = surfshop.ShoppingCart()

    def test_add_surfboard(self):
        message = self.cart.add_surfboards(1)
        self.assertEqual(message, 'Successfully added 1 surfboard to cart!')

    def test_add_surfboards(self):
        for quantity in range(2, 5):
            with self.subTest(quantity=quantity):
                message = self.cart.add_surfboards(quantity)
                self.assertEqual(
                    message, f'Successfully added {quantity} surfboards to cart!')
                self.cart = surfshop.ShoppingCart()

    # def test_add_surfboards_2(self):
    #     message = self.cart.add_surfboards(2)
    #     self.assertEqual(
    #         message, 'Successfully added 2 surfboards to cart!')

    @unittest.skip
    def test_add_too_many_surfboards(self):
        self.assertRaises(surfshop.TooManyBoardsError,
                          self.cart.add_surfboards, 5)

    @unittest.expectedFailure
    def test_apply_local_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount)


unittest.main()
