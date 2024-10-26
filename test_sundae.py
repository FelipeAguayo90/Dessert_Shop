import unittest
import dessert as d


class TestSundae(unittest.TestCase):
    def setUp(self):
        self.i = d.Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29)

    def test_init(self):
        self.assertEqual(self.i.name, "Vanilla")
        self.assertEqual(self.i.scoop_count, 3)
        self.assertEqual(self.i.price_per_scoop, 0.69)
        self.assertEqual(self.i.topping_name, "Hot Fudge")
        self.assertEqual(self.i.topping_price, 1.29)

    def test_set_name(self):
        self.i.name = "Chocolate Mint"
        self.assertEqual(self.i.name, "Chocolate Mint")

    def test_set_scoop_count(self):
        self.i.scoop_count = 2
        self.assertEqual(self.i.scoop_count, 2)

    def test_set_price_per_scoop(self):
        self.i.price_per_scoop = 0.50
        self.assertEqual(self.i.price_per_scoop, 0.50)

    def test_set_topping_name(self):
        self.i.topping_name = "Sprinkles"
        self.assertEqual(self.i.topping_name, "Sprinkles")

    def test_set_topping_price(self):
        self.i.topping_price = 1.25
        self.assertEqual(self.i.topping_price, 1.25)

    def test_calculate_cost(self):
        self.assertEqual(self.i.calculate_cost(), 3.36)

    def test_calculate_tax(self):
        self.assertEqual(self.i.calculate_tax(), 0.24)

    def test_packaging(self):
        self.assertEqual(self.i._packaging, "Boat")

    def tearDown(self):
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
