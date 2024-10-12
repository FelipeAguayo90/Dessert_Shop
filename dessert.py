from typing import List


class DessertItem:
    """
    DessertItem class represents a dessert item in the dessert shop.

    Attributes:
        _name (str): The name of the candy.
    """

    def __init__(self, name: str = ""):
        try:
            if type(name) is not str:
                raise TypeError("New name must be a string.")
            else:
                self._name = name
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

    def get_candy_weight(self):
        return self._candy_weight

    def set_candy_weight(self, new_weight: float):
        self._candy_weight = new_weight

    def get_price_per_pound(self):
        return self._price_per_pound

    def set_price_per_pound(self, new_price):
        self._price_per_pound = new_price

    candy_weight = property(get_candy_weight, set_candy_weight)

    price_per_pound = property(get_price_per_pound, set_price_per_pound)


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

    def get_cookie_quantity(self):
        return self._cookie_quantity

    def set_cookie_quantity(self, new_quantity):
        self._cookie_quantity = new_quantity

    def get_price_per_dozen(self):
        return self._price_per_dozen

    def set_price_per_dozen(self, new_price):
        self._price_per_dozen = new_price

    cookie_quantity = property(get_cookie_quantity, set_cookie_quantity)

    price_per_dozen = property(get_price_per_dozen, set_price_per_dozen)


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

    def get_scoop_count(self):
        return self._scoop_count

    def set_scoop_count(self, new_quantity):
        self._scoop_count = new_quantity

    def get_price_per_scoop(self):
        return self._price_per_scoop

    def set_price_per_scoop(self, new_price):
        self._price_per_scoop = new_price

    scoop_count = property(get_scoop_count, set_scoop_count)

    price_per_scoop = property(get_price_per_scoop, set_price_per_scoop)


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

    def get_topping_name(self):
        return self._topping_name

    def set_topping_name(self, new_name):
        self._topping_name = new_name

    def get_topping_price(self):
        return self._topping_price

    def set_topping_price(self, new_price):
        self._topping_price = new_price

    topping_name = property(get_topping_name, set_topping_name)

    topping_price = property(get_topping_price, set_topping_price)


class Order:
    """
    This class represents an order, stores information of items being added to the order
    of type DessertItem.

    Attributes:
        _order (list[DessertItem])
    """

    def __init__(self):
        self._oder: List[DessertItem] = []

    def add(self, new_item: DessertItem):
        self._oder.append(new_item)

    def __len__(self):
        return len(self._oder)

    def __str__(self):
        order = ""
        for item in self._oder:
            order += f"{item.name} \n"
        order += f"Total number of items in order: {len(self)}"
        return order
