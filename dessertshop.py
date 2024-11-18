import dessert as d
from receipt import make_receipt
from typing import List, Dict


class Customer:
    id: int = 0

    def __init__(self, name: str) -> None:
        self._customer_name: str = name
        self._order_history: List[d.Order] = []
        self._customer_id: int = 1000 + self.__class__.id
        self.__class__.id += 1

    def add2history(self, order: "d.Order") -> "Customer":
        self._order_history.append(order)
        return self


class DessertShop:

    def __init__(self):
        self._customer_db: Dict[str, Customer] = {}

    def user_prompt_candy(self) -> d.Candy:
        candy_name: str = ""
        candy_name: float = 0.0
        candy_name: float = 0.0
        while True:
            try:
                candy_name = input("Enter the type of candy: \n")
                if len(candy_name) > 0:
                    float(candy_name)
                else:
                    print("Please enter a valid type. ", end="")
            except ValueError:
                break
        while True:
            try:
                candy_weight = float(input("Enter the weight of the candy: \n"))
                break
            except ValueError:
                print("Please enter a valid weight. ", end="")
        while True:
            try:
                candy_price = float(input("Enter the price per pound: \n"))
                break
            except ValueError:
                print("Please enter a valid price. ", end="")
        return d.Candy(candy_name, candy_weight, candy_price)

    def user_prompt_cookie(self) -> d.Cookie:
        cookie_name: str = ""
        cookie_quantity: int = 0
        cookie_price: float = 0.0
        while True:
            try:
                cookie_name = input("Enter the type of cookie: \n")
                if len(cookie_name) > 0:
                    float(cookie_name)
                else:
                    print("Please enter a valid type. ", end="")
            except ValueError:
                break
        while True:
            try:
                cookie_quantity = int(input("Enter the quantity purchased: \n"))
                break
            except ValueError:
                print("Please enter a valid quantity. ", end="")
        while True:
            try:
                cookie_price = float(input("Enter the price per dozen: \n"))
                break
            except ValueError:
                print("Please enter a valid price. ", end="")
        return d.Cookie(cookie_name, cookie_quantity, cookie_price)

    def user_prompt_icecream(self) -> d.IceCream:
        ice_cream_name: str = ""
        ice_cream_scoops: int = 0
        ice_cream_price: float = 0.0
        while True:
            try:
                ice_cream_name = input("Enter the type of ice cream: \n")
                if len(ice_cream_name) > 0:
                    float(ice_cream_name)
                else:
                    print("Please enter a valid type. ", end="")
            except ValueError:
                break
        while True:
            try:
                ice_cream_scoops = int(input("Enter the number of scoops: \n"))
                break
            except ValueError:
                print("Please enter a valid number. ", end="")
        while True:
            try:
                ice_cream_price = float(input("Enter the price per scoop: \n"))
                break
            except ValueError:
                print("Please enter a valid price. ", end="")
        return d.IceCream(ice_cream_name, ice_cream_scoops, ice_cream_price)

    def user_prompt_sundae(self) -> d.Sundae:
        ice_cream_name: str = ""
        ice_cream_scoops: int = 0
        ice_cream_price: float = 0.0
        topping_name: str = ""
        topping_price: float = 0.0
        while True:
            try:
                ice_cream_name = input("Enter the type of ice cream: \n")
                if len(ice_cream_name) > 0:
                    float(ice_cream_name)
                else:
                    print("Please enter a valid type. ", end="")
            except ValueError:
                break
        while True:
            try:
                ice_cream_scoops = int(input("Enter the number of scoops: \n"))
                break
            except ValueError:
                print("Please enter a valid number. ", end="")
        while True:
            try:
                ice_cream_price = float(input("Enter the price per scoop: \n"))
                break
            except ValueError:
                print("Please enter a valid price. ", end="")
        while True:
            try:
                topping_name = input("Enter the topping: \n")
                if len(topping_name) > 0:
                    float(topping_name)
                else:
                    print("Please enter a valid type. ", end="")
            except ValueError:
                break
        while True:
            try:
                topping_price = float(input("Enter the price for the topping: \n"))
                break
            except ValueError:
                print("Please enter a valid price. ", end="")
        return d.Sundae(
            ice_cream_name,
            ice_cream_scoops,
            ice_cream_price,
            topping_name,
            topping_price,
        )

    def payment_type(self, order: "d.Order"):
        payment: bool = False
        prompt2 = "\n".join(
            [
                "\n",
                "1: Cash",
                "2: Card",
                "3: Phone",
                "\nHow would you like to pay? CASH, CARD, or PHONE: ",
            ]
        )
        while not payment:
            choice = input(prompt2)
            match choice:
                case "":
                    payment = True
                case "1":
                    pay_type = order.set_pay_type("CASH")
                    break
                case "2":
                    pay_type = order.set_pay_type("CARD")
                    break
                case "3":
                    pay_type = order.set_pay_type("PHONE")
                    break
                case _:
                    pay_type = order.set_pay_type(choice.upper())
                    if pay_type == True:
                        payment = True
                    else:
                        message, boolean = pay_type
                        print(message)


def main():
    # new_oder = d.Order()
    # new_oder.add(d.Candy("Candy Corn", 1.5, 0.25))
    # new_oder.add(d.Candy("Gummy Bears", 0.25, 0.35))
    # new_oder.add(d.Cookie("Chocolate Chip", 6, 3.99))
    # new_oder.add(d.IceCream("Pistachio", 2, 0.79))
    # new_oder.add(d.Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29))
    # new_oder.add(d.Cookie("Oatmeal Raisin", 2, 3.45))
    # print(new_oder)

    shop = DessertShop()

    # boolean done = false
    back_from_admin: bool = False
    done: bool = False
    done2: bool = False
    # build the prompt string once
    prompt = "\n".join(
        [
            "\n",
            "1: Candy",
            "2: Cookie",
            "3: Ice Cream",
            "4: Sunday",
            "5: Admin Module",
            "\nWhat would you like to add to the order? (1-4, Enter for done): ",
        ]
    )
    prompt2 = "\n".join(
        [
            "\n",
            "\nWould you want to start another order? (Y/N): ",
        ]
    )
    prompt3 = "\n".join(["\n", "\nWhat is the customer name?: "])
    prompt4 = "\n".join(
        [
            "\n",
            "1: Shop Customer List",
            "2: Customer Order History",
            "3: Best Customer3",
            "4: Exit Admin Module",
            "\nWhat would you like to see? (1-4): ",
        ]
    )

    while not done2:
        order = d.Order()
        customer_name: str = ""
        while not done:
            choice = input(prompt)
            match choice:
                case "":
                    if not back_from_admin:
                        while True:
                            customer_name += input(prompt3).upper()
                            if len(customer_name) > 0:
                                if customer_name not in shop._customer_db.keys():
                                    customer = Customer(customer_name)
                                    customer.add2history(order)
                                    shop._customer_db[customer_name] = customer
                                else:
                                    shop._customer_db[customer_name].add2history(order)
                                done = True
                                break
                            else:
                                print("\nPlease enter a valid name.")
                    else:
                        done = True
                case "1":
                    item = shop.user_prompt_candy()
                    order.add(item)
                    print(f"{item.name} has been added to your order.")
                    back_from_admin: bool = False
                case "2":
                    item = shop.user_prompt_cookie()
                    order.add(item)
                    print(f"{item.name} has been added to your order.")
                    back_from_admin: bool = False
                case "3":
                    item = shop.user_prompt_icecream()
                    order.add(item)
                    print(f"{item.name} has been added to your order.")
                    back_from_admin: bool = False
                case "4":
                    item = shop.user_prompt_sundae()
                    order.add(item)
                    print(f"{item.name} has been added to your order.")
                    back_from_admin: bool = False
                case "5":
                    while True:
                        choice = input(prompt4)
                        match choice:
                            case "1":
                                for customer in shop._customer_db.values():
                                    print(
                                        f"\nCustomer Name: {customer._customer_name.capitalize()}\tCustomer ID: {customer._customer_id}"
                                    )
                            case "2":
                                customer = input(
                                    "\nEnter the name of the customer:\n"
                                ).upper()
                                if customer in shop._customer_db:
                                    order_num = 1
                                    print(
                                        f"\nCustomer Name: {shop._customer_db[customer]._customer_name.capitalize()}\tCustomer ID: {shop._customer_db[customer]._customer_id} "
                                    )
                                    for order in shop._customer_db[
                                        customer
                                    ]._order_history:
                                        print(f"\nOrder #: {order_num}\n")
                                        print(order)
                                        order_num += 1
                                else:
                                    print("\nCustomer does not exist.")
                            case "3":
                                best_customer = max(
                                    shop._customer_db.items(),
                                    key=lambda customer: len(
                                        customer[1]._order_history
                                    ),
                                )
                                print(
                                    f"\nThe Dessert Shop's most valued customer is: {best_customer[0].capitalize()}!"
                                )
                            case "4":
                                back_from_admin = True
                                done2 = True
                                break
                            case _:
                                print(
                                    "\nInvalid response:  Please enter a choice from the menu (1-4) or Enter"
                                )
                case _:
                    print(
                        "Invalid response:  Please enter a choice from the menu (1-4) or Enter"
                    )
        if not back_from_admin:
            shop.payment_type(order)
            order.sort()
            print(order)
            print(
                f"Customer Name: {shop._customer_db[customer_name]._customer_name.capitalize():<10}Customer ID: {shop._customer_db[customer_name]._customer_id :<10}Total Orders: {len(shop._customer_db[customer_name]._order_history)}"
            )
            receipt_list = [["Name", "Quantity", "Unit Price", "Cost", "Tax"]]
            subtotal_cost = 0
            subtotal_tax = 0

            for item in order._oder:
                cost = item.calculate_cost()
                tax = item.calculate_tax()
                subtotal_cost += cost
                subtotal_tax += tax
                parts = item.__str__().split("\n")
                list1_str = parts[0]
                list2_str = parts[1] if len(parts) > 1 else False
                list1 = [text.strip() for text in list1_str.split(",")]
                list2 = (
                    [text.strip() for text in list2_str.split(",")] if list2_str else []
                )
                receipt_list.append(list1)
                if len(list2) > 0:
                    receipt_list.append(list2)

            receipt_list.append(list(("Total items in the order", len(order))))
            receipt_list.append(
                list(
                    (
                        "Order Subtotals",
                        "",
                        "",
                        f"${order.order_cost():.2f}",
                        f"${order.order_tax():.2f}",
                    )
                )
            )

            receipt_list.append(
                list(
                    (
                        "Order Total",
                        "",
                        "",
                        "",
                        f"${(order.order_cost() + order.order_tax()):.2f}",
                    )
                )
            )
            receipt_list.append(list((f"Paid with {order.get_pay_type()}", "", "", "")))
            receipt_list.append(
                list(
                    (
                        f"Customer Name: {shop._customer_db[customer_name]._customer_name.capitalize():<10}",
                        f"Customer ID: {shop._customer_db[customer_name]._customer_id :<10}",
                        f"Total Orders: {len(shop._customer_db[customer_name]._order_history)}",
                    )
                )
            )

            make_receipt(receipt_list)

            choice = input(prompt2).upper()
            match choice:
                case "":
                    done2 = True
                case "Y":
                    done = False
                case _:
                    done2 = True
        print()


if __name__ == "__main__":
    main()
