import unittest
import dessert as d


class TestCookie(unittest.TestCase):
    def setUp(self):
        self.c = d.Cookie("Chocolate Chip", 6, 3.99)

    def test_init(self):
        self.assertEqual(self.c.name, "Chocolate Chip")
        self.assertEqual(self.c.cookie_quantity, 6)
        self.assertEqual(self.c.price_per_dozen, 3.99)

    def test_set_name(self):
        self.c.name = "Sugar Cookie"
        self.assertEqual(self.c.name, "Sugar Cookie")

    def test_set_cookie_quantity(self):
        self.c.cookie_quantity = 24
        self.assertEqual(self.c.cookie_quantity, 24)

    def test_set_price_per_dozen(self):
        self.c.price_per_dozen = 7.50
        self.assertEqual(self.c.price_per_dozen, 7.50)

    def test_calculate_cost(self):
        self.assertEqual(self.c.calculate_cost(), 2.00)

    def test_calculate_tax(self):
        self.assertEqual(self.c.calculate_tax(), 0.14)

    def tearDown(self):
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
