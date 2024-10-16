import unittest
import dessert as d


class TestIceCream(unittest.TestCase):
    def setUp(self):
        self.i = d.IceCream("Cookies N Cream", 3, 1.50)

    def test_init(self):
        self.assertEqual(self.i.name, "Cookies N Cream")
        self.assertEqual(self.i.scoop_count, 3)
        self.assertEqual(self.i.price_per_scoop, 1.50)

    def test_set_name(self):
        self.i.name = "Chocolate Mint"
        self.assertEqual(self.i.name, "Chocolate Mint")

    def test_set_scoop_count(self):
        self.i.scoop_count = 2
        self.assertEqual(self.i.scoop_count, 2)

    def test_set_price_per_scoop(self):
        self.i.price_per_scoop = 1.25
        self.assertEqual(self.i.price_per_scoop, 1.25)

    def tearDown(self):
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
