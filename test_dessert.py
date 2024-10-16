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


if __name__ == "__main__":
    unittest.main()
