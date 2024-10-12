import unittest
import dessert as d


class TestDessertItem(unittest.TestCase):
    def setUp(self):
        self.item = d

    def test_init(self):
        item = self.item.DessertItem("Tres Leches")
        self.assertEqual(item.name, "Tres Leches")

    def test_init_invalid_value(self):
        with self.assertRaises(TypeError):
            self.item.DessertItem(2)

    def test_get_name(self):
        item = self.item.DessertItem("Tres Leches")
        self.assertEqual(item.name, "Tres Leches")

    def test_set_name(self):
        item = self.item.DessertItem("Tres Leches")
        item.name = "Carrot Cake"
        self.assertEqual(item.name, "Carrot Cake")

    def test_invalid_set_name(self):
        item = self.item.DessertItem("Tres Leches")
        item.name = 6
        self.assertEqual(item.name, "Tres Leches")

    def tearDown(self):
        return super().tearDown()


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


class TestCookie(unittest.TestCase):
    def setUp(self):
        self.c = d.Cookie("Chocolate Chip", 12, 6.50)

    def test_init(self):
        self.assertEqual(self.c.name, "Chocolate Chip")
        self.assertEqual(self.c.cookie_quantity, 12)
        self.assertEqual(self.c.price_per_dozen, 6.50)

    def test_set_name(self):
        self.c.name = "Sugar Cookie"
        self.assertEqual(self.c.name, "Sugar Cookie")

    def test_set_cookie_quantity(self):
        self.c.cookie_quantity = 24
        self.assertEqual(self.c.cookie_quantity, 24)

    def test_set_price_per_dozen(self):
        self.c.price_per_dozen = 7.50
        self.assertEqual(self.c.price_per_dozen, 7.50)

    def tearDown(self):
        return super().tearDown()


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


class TestSundae(unittest.TestCase):
    def setUp(self):
        self.i = d.Sundae("Cookies N Cream", 3, 1.50, "Hot Fudge", 1.15)

    def test_init(self):
        self.assertEqual(self.i.name, "Cookies N Cream")
        self.assertEqual(self.i.scoop_count, 3)
        self.assertEqual(self.i.price_per_scoop, 1.50)
        self.assertEqual(self.i.topping_name, "Hot Fudge")
        self.assertEqual(self.i.topping_price, 1.15)

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

    def tearDown(self):
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
