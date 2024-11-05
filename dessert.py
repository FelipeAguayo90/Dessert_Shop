from typing import List
from abc import ABC, abstractmethod
from packaging import Packaging
from payable import Payable, PayType


class DessertItem(ABC):
    """
    DessertItem class represents a dessert item in the dessert shop.

    Attributes:
        _name (str): The name of the candy.
    """

    _tax_percent = 0.0725

    def __init__(self, name: str = ""):
        try:
            if type(name) is not str:
                raise TypeError("New name must be a string.")
            else:
                self._name = name
                self._packaging = None
        except TypeError as e:
            message = f"{e}"
            return message

    def get_name(self):
        try:
            return self._name
        except AttributeError:
            print("Object has no name.")

    def set_name(self, new_name: str = ""):
        try:
            if type(new_name) is not str:
                raise TypeError("New name must be a string.")
            self._name = new_name
        except TypeError as e:
            message = f"{e}"
            return message

    @abstractmethod
    def calculate_cost(self) -> float:
        pass

    def calculate_tax(self) -> float:
        tax = self.calculate_cost() * DessertItem._tax_percent
        return round(tax, 2)

    @classmethod
    def change_tax(cls, new_tax):
        cls._tax_percent = new_tax

    name = property(get_name, set_name)


class Candy(DessertItem):
    """
    Candy class, inherits from DessertItem.

    This class represents a type of candy, storing information about its weight and price per pound.

    Attributes:
        _name (str): The name of the candy (inherited from DessertItem).
        _weight (float): The weight of the candy in pounds.
        _price_per_pound (float): The price of the candy per pound.
    """

    def __init__(self, name: str = "", weight: float = 0.0, price: float = 0.0):
        super().__init__(name)
        self._candy_weight = weight
        self._price_per_pound = price
        self._packaging = "Bag"

    def get_candy_weight(self):
        return self._candy_weight

    def set_candy_weight(self, new_weight: float):
        self._candy_weight = new_weight

    def get_price_per_pound(self):
        return self._price_per_pound

    def set_price_per_pound(self, new_price):
        self._price_per_pound = new_price

    def calculate_cost(self) -> float:
        cost = self._candy_weight * self._price_per_pound
        return round(cost, 2)

    candy_weight = property(get_candy_weight, set_candy_weight)

    price_per_pound = property(get_price_per_pound, set_price_per_pound)

    def __str__(self) -> str:
        return f"{self.name} ({self._packaging}), {str(self.candy_weight)}lbs, ${self.price_per_pound:.2f}/lbs, ${self.calculate_cost():.2f}, {self.calculate_tax():.2f}"


class Cookie(DessertItem):
    """
    Cookie class, inherits from DessertItem.

    This class represents cookies, storing information about their quantity and price per dozen.

    Attributes:
        _name (str): The name of the cookie (inherited from DessertItem).
        _cookie_quantity (int): The quantity of cookies.
        _price_per_dozen (float): The price of the cookies per dozen.
    """

    def __init__(self, name: str = "", quantity: int = 0, price: float = 0.0):
        super().__init__(name)
        self._cookie_quantity = quantity
        self._price_per_dozen = price
        self._packaging = "Box"

    def get_cookie_quantity(self):
        return self._cookie_quantity

    def set_cookie_quantity(self, new_quantity):
        self._cookie_quantity = new_quantity

    def get_price_per_dozen(self):
        return self._price_per_dozen

    def set_price_per_dozen(self, new_price):
        self._price_per_dozen = new_price

    def calculate_cost(self) -> float:
        cost_per_cookie = self._price_per_dozen / 12
        cost = self._cookie_quantity * round(cost_per_cookie, 3)
        return round(cost, 2)

    cookie_quantity = property(get_cookie_quantity, set_cookie_quantity)

    price_per_dozen = property(get_price_per_dozen, set_price_per_dozen)

    def __str__(self) -> str:
        return f"{self.name} ({self._packaging}), {str(self.cookie_quantity)}, ${str(self.price_per_dozen)}/dozen, ${self.calculate_cost():.2f}, {self.calculate_tax():.2f}"


class IceCream(DessertItem):
    """
    IceCream class, inherits from DessertItem.

    This class represents ice cream, storing information about scoop quantity and price per scoop.

    Attributes:
        _name (str): The name of the ice cream (inherited from DessertItem).
        _scoop_count (int): The quantity of scoops.
        _price_per_scoop (float): The price of the ice cream per scoop.
    """

    def __init__(self, name: str = "", scoops: int = 0, price: float = 0.0):
        super().__init__(name)
        self._scoop_count = scoops
        self._price_per_scoop = price
        self._packaging = "Bowl"

    def get_scoop_count(self):
        return self._scoop_count

    def set_scoop_count(self, new_quantity):
        self._scoop_count = new_quantity

    def get_price_per_scoop(self):
        return self._price_per_scoop

    def set_price_per_scoop(self, new_price):
        self._price_per_scoop = new_price

    def calculate_cost(self) -> float:
        cost = self._scoop_count * self._price_per_scoop
        return round(cost, 2)

    scoop_count = property(get_scoop_count, set_scoop_count)

    price_per_scoop = property(get_price_per_scoop, set_price_per_scoop)

    def __str__(self) -> str:
        return f"{self.name} ({self._packaging}), {self.scoop_count}, ${self.price_per_scoop}/scoop, ${self.calculate_cost():.2f}, {self.calculate_tax():.2f}"


class Sundae(IceCream):
    """
    Sundae class, inherits from IceCream.

    This class represents ice cream, storing information about scoop quantity and price per scoop.

    Attributes:
        _name (str): The name of the ice cream (inherited from DessertItem).
        _scoop_count (int): The quantity of scoops (inherited from IceCream).
        _price_per_scoop (float): The price of the ice cream per scoop (inherited from IceCream).
        _topping_name (str): The name of the topping.
        _topping_price (float): The price of the topping.
    """

    def __init__(
        self,
        name: str = "",
        scoops: int = 0,
        price: float = 0,
        topping_name: str = "",
        topping_price: float = 0.0,
    ):
        super().__init__(name, scoops, price)
        self._topping_name = topping_name
        self._topping_price = topping_price
        self._packaging = "Boat"

    def get_topping_name(self):
        return self._topping_name

    def set_topping_name(self, new_name):
        self._topping_name = new_name

    def get_topping_price(self):
        return self._topping_price

    def set_topping_price(self, new_price):
        self._topping_price = new_price

    def calculate_cost(self) -> float:
        cost = round(self._scoop_count * self._price_per_scoop, 2) + self._topping_price
        return round(cost, 2)

    topping_name = property(get_topping_name, set_topping_name)

    topping_price = property(get_topping_price, set_topping_price)

    def __str__(self) -> str:
        return f"{self.topping_name} {self.name} Sundae ({self._packaging}), {self.scoop_count}, ${self.price_per_scoop:.2f}/scoop, ${self.calculate_cost():.2f}, {self.calculate_tax():.2f}\n{self.topping_name}, 1, ${self.topping_price:.2f}"


class Order:
    """
    This class represents an order, stores information of items being added to the order
    of type DessertItem.

    Attributes:
        _order (list[DessertItem])
    """

    def __init__(self):
        self._oder: List[DessertItem] = []
        self._payment_type: PayType = PayType.CASH.value

    def add(self, new_item: DessertItem):
        self._oder.append(new_item)

    def order_cost(self):
        order_cost = 0
        for item in self._oder:
            order_cost += item.calculate_cost()
        return round(order_cost, 2)

    def order_tax(self):
        total_tax = self.order_cost() * DessertItem._tax_percent
        return round(total_tax, 2)

    def get_pay_type(self) -> PayType:
        pay_type = self._payment_type
        try:
            if pay_type not in {
                PayType.CARD.value,
                PayType.CASH.value,
                PayType.PHONE.value,
            }:
                raise ValueError("\nInvalid payment type")
            return self._payment_type
        except ValueError as e:
            return (e, False)

    def set_pay_type(self, payment_method: PayType) -> None:
        try:
            if payment_method not in {
                PayType.CARD.value,
                PayType.CASH.value,
                PayType.PHONE.value,
            }:
                raise ValueError("\nInvalid payment type")
            self._payment_type = payment_method
            return True
        except ValueError as e:
            return (e, False)

    def __len__(self):
        return len(self._oder)

    def __str__(self):
        order = ""
        for item in self._oder:
            order += item.__str__() + "\n"
        order += f"""Total number of items in order: {len(self)} \nOrder Subtotals {self.order_cost():.2f} {self.order_tax():.2f}\nOrder Total {self.order_cost() + self.order_tax():.2f}\nPaid with {self.get_pay_type()}"""
        return order
