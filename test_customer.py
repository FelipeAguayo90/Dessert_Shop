import unittest
from dessertshop import Customer
import dessert as d


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.c = Customer("Larry")
        self.order = d.Order().add(d.Cookie("Chocolate Chip", 6, 3.99))

    def test_init(self):
        print(self.c._customer_id)
        self.assertEqual(self.c._customer_name, ("Larry"))
        self.assertEqual(type(self.c._customer_id), int)
        self.assertEqual(type(self.c._order_history), list)

    def tearDown(self):
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
