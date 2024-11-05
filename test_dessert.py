import unittest
import dessert as d


class TestDessertItem(unittest.TestCase):
    def setUp(self):
        self.item = d.Candy("Candy Corn", 1.5, 0.25)

    def test_init(self):
        self.assertEqual(self.item.name, "Candy Corn")

    def test_init_invalid_value(self):
        with self.assertRaises(TypeError):
            self.item2 = d.DessertItem(2)

    def test_get_name(self):
        self.assertEqual(self.item.name, "Candy Corn")

    def test_set_name(self):
        self.item.name = "Carrot Cake"
        self.assertEqual(self.item.name, "Carrot Cake")

    def test_invalid_set_name(self):
        self.item.name = 6
        self.assertEqual(self.item.name, "Candy Corn")

    def test_calculate_cost(self):
        item = d.Candy("Candy Corn", 1.5, 0.25)
        self.assertEqual(item.calculate_cost(), 0.38)

    def test_tax(self):
        self.assertEqual(self.item._tax_percent, 0.0725)
        self.item.change_tax(0.0825)
        self.assertEqual(self.item._tax_percent, 0.0825)

    def test_packaging(self):
        self.assertEqual(self.item._packaging, "Bag")

    def test_equal_to(self):
        self.assertTrue(self.item == d.Candy("Candy", 1.5, 0.25))
        self.assertFalse(self.item == d.Candy("Candy", 1.4, 0.25))

    def test_less_than(self):
        self.assertTrue(self.item < d.Candy("Candy", 1.6, 0.25))
        self.assertFalse(self.item < d.Candy("Candy", 1.4, 0.25))

    def test_less_than_or_equal(self):
        self.assertTrue(self.item <= d.Candy("Candy", 1.5, 0.25))
        self.assertTrue(self.item <= d.Candy("Candy", 1.6, 0.25))
        self.assertFalse(self.item <= d.Candy("Candy", 1.4, 0.25))

    def test_grater_than(self):
        self.assertTrue(self.item > d.Candy("Candy", 1.4, 0.25))
        self.assertFalse(self.item > d.Candy("Candy", 1.6, 0.25))

    def test_greater_than_or_equal(self):
        self.assertTrue(self.item >= d.Candy("Candy", 1.5, 0.25))
        self.assertTrue(self.item >= d.Candy("Candy", 1.4, 0.25))
        self.assertFalse(self.item >= d.Candy("Candy", 1.6, 0.25))

    def tearDown(self):
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
