import unittest
import dessert as d


class TestCookie(unittest.TestCase):
    def setUp(self):
        self.c = d.Cookie("Chocolate Chip", 6, 3.99)
        self.other = d.Cookie("Chocolate Chip", 5, 3.99)
        self.candy = d.Candy("Gummy Bears", 1.25, 0.35)

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

    def test_packaging(self):
        self.assertEqual(self.c._packaging, "Box")

    def test_can_combine_true(self):
        self.assertTrue(self.c.can_combine(self.other))

    def test_can_combine_dif_class(self):
        self.assertFalse(self.c.can_combine(self.candy))

    def test_combine_correctly(self):
        self.c.combine(self.other)
        self.assertEqual(self.c.cookie_quantity, 11)

    def test_combine_incorrectly(self):
        self.c.combine(self.candy)
        self.assertEqual(self.c._cookie_quantity, 6)

    def tearDown(self):
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
