import unittest
import dessert as d


class TestCandy(unittest.TestCase):
    def setUp(self):
        self.c = d.Candy("Gummy Bears", 0.25, 0.35)
        self.other = d.Candy("Gummy Bears", 1.25, 0.35)
        self.cookie = d.Cookie("Chocolate Chip", 6, 3.99)

    def test_init(self):
        self.assertEqual(self.c.name, "Gummy Bears")
        self.assertEqual(self.c.candy_weight, 0.25)
        self.assertEqual(self.c.price_per_pound, 0.35)

    def test_set_name(self):
        self.c.name = "Chocolates"
        self.assertEqual(self.c.name, "Chocolates")

    def test_set_candy_weight(self):
        self.c.candy_weight = 8.0
        self.assertEqual(self.c.candy_weight, 8.0)

    def test_set_price_per_pound(self):
        self.c.price_per_pound = 7.50
        self.assertEqual(self.c.price_per_pound, 7.50)

    def test_calculate_cost(self):
        self.assertEqual(self.c.calculate_cost(), 0.09)

    def test_calculate_tax(self):
        self.assertEqual(self.c.calculate_tax(), 0.01)

    def test_packaging(self):
        self.assertEqual(self.c._packaging, "Bag")

    def test_can_combine_true(self):
        self.assertTrue(self.c.can_combine(self.other))

    def test_can_combine_dif_class(self):
        self.assertFalse(self.c.can_combine(self.cookie))

    def test_combine_correctly(self):
        self.c.combine(self.other)
        self.assertEqual(self.c.candy_weight, 1.50)

    def test_combine_incorrectly(self):
        self.c.combine(self.cookie)
        self.assertEqual(self.c.candy_weight, 0.25)

    def tearDown(self):
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
