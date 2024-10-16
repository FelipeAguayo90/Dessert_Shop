import unittest
import dessert as d


class TestIceCream(unittest.TestCase):
    def setUp(self):
        self.i = d.IceCream("Pistachio", 2, 0.79)

    def test_init(self):
        self.assertEqual(self.i.name, "Pistachio")
        self.assertEqual(self.i.scoop_count, 2)
        self.assertEqual(self.i.price_per_scoop, 0.79)

    def test_set_name(self):
        self.i.name = "Chocolate Mint"
        self.assertEqual(self.i.name, "Chocolate Mint")

    def test_set_scoop_count(self):
        self.i.scoop_count = 3
        self.assertEqual(self.i.scoop_count, 3)

    def test_set_price_per_scoop(self):
        self.i.price_per_scoop = 1.25
        self.assertEqual(self.i.price_per_scoop, 1.25)

    def test_calculate_cost(self):
        self.assertEqual(self.i.calculate_cost(), 1.58)

    def test_calculate_tax(self):
        self.assertEqual(self.i.calculate_tax(), 0.11)

    def tearDown(self):
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
