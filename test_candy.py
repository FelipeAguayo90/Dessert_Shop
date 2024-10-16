import unittest
import dessert as d


class TestCandy(unittest.TestCase):
    def setUp(self):
        self.c = d.Candy("M&Ms", 6.0, 8.50)

    def test_init(self):
        self.assertEqual(self.c.name, "M&Ms")
        self.assertEqual(self.c.candy_weight, 6.0)
        self.assertEqual(self.c.price_per_pound, 8.50)

    def test_set_name(self):
        self.c.name = "Chocolates"
        self.assertEqual(self.c.name, "Chocolates")

    def test_set_candy_weight(self):
        self.c.candy_weight = 8.0
        self.assertEqual(self.c.candy_weight, 8.0)

    def test_set_price_per_pound(self):
        self.c.price_per_pound = 7.50
        self.assertEqual(self.c.price_per_pound, 7.50)

    def tearDown(self):
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
