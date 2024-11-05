import unittest
import dessert as d


class TestOrder(unittest.TestCase):

    def setUp(self):
        self.order = d.Order()
        self.order.add(d.Candy("Candy Corn", 1.5, 0.25))
        self.order.add(d.Candy("Gummy Bears", 0.25, 0.35))
        self.order.add(d.Cookie("Chocolate Chip", 6, 3.99))
        self.order.add(d.IceCream("Pistachio", 2, 0.79))
        self.order.add(d.Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29))
        self.order.add(d.Cookie("Oatmeal Raisin", 2, 3.45))

    def test_set_pay_type_cash(self):
        self.order.set_pay_type("CASH")
        self.assertEqual(self.order._payment_type, "CASH")

    def test_set_pay_type_card(self):
        self.order.set_pay_type("CARD")
        self.assertEqual(self.order._payment_type, "CARD")

    def test_set_pay_type_phone(self):
        self.order.set_pay_type("PHONE")
        self.assertEqual(self.order._payment_type, "PHONE")

    def test_set_pay_type_invalid(self):
        self.order.set_pay_type("OTHER")
        self.assertEqual(self.order._payment_type, "CASH")

    def test_get_pay_type(self):
        self.order._payment_type = "OTHER"
        payment_type = self.order.get_pay_type()
        self.assertIsNot(payment_type, "OTHER")

    def test_sort(self):
        self.order.sort()
        self.assertEqual(
            self.order._oder[-1], d.Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29)
        )
        self.assertEqual(self.order._oder[0], d.Candy("Gummy Bears", 0.25, 0.35))

    def tearDown(self):
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
