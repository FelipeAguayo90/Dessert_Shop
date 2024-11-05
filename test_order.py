import unittest
import dessert as d


class TestOrder(unittest.TestCase):

    def setUp(self):
        self.order = d.Order()

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

    def tearDown(self):
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
