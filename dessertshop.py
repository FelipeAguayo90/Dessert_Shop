import dessert as d
from receipt import make_receipt


class DessertShop:
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
    order = d.Order()
    """
    order.add(Candy('Candy Corn', 1.5, 0.25))
    order.add(Candy('Gummy Bears', 0.25, 0.35))
    order.add(Cookie('Chocolate Chip', 6, 3.99))
    order.add(IceCream('Pistachio', 2, 0.79))
    order.add(Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29))
    order.add(Cookie('Oatmeal Raisin', 2, 3.45))
    """
    # boolean done = false
    done: bool = False
    # build the prompt string once
    prompt = "\n".join(
        [
            "\n",
            "1: Candy",
            "2: Cookie",
            "3: Ice Cream",
            "4: Sunday",
            "\nWhat would you like to add to the order? (1-4, Enter for done): ",
        ]
    )

    while not done:
        choice = input(prompt)
        match choice:
            case "":
                done = True
            case "1":
                item = shop.user_prompt_candy()
                order.add(item)
                print(f"{item.name} has been added to your order.")
            case "2":
                item = shop.user_prompt_cookie()
                order.add(item)
                print(f"{item.name} has been added to your order.")
            case "3":
                item = shop.user_prompt_icecream()
                order.add(item)
                print(f"{item.name} has been added to your order.")
            case "4":
                item = shop.user_prompt_sundae()
                order.add(item)
                print(f"{item.name} has been added to your order.")
            case _:
                print(
                    "Invalid response:  Please enter a choice from the menu (1-4) or Enter"
                )
    print()

    receipt_list = [["Name", "Item Cost", "Tax"]]
    subtotal_cost = 0
    subtotal_tax = 0

    for item in order._oder:
        cost = item.calculate_cost()
        tax = item.calculate_tax()
        subtotal_cost += cost
        subtotal_tax += tax
        receipt_list.append(list((item.name, f"${cost:.2f}", f"${tax:.2f}")))
    receipt_list.append(
        list(
            (
                "Order Subtotals",
                f"${order.order_cost():.2f}",
                f"${order.order_tax():.2f}",
            )
        )
    )
    receipt_list.append(
        list(("Order Total", "", f"${order.order_cost() + order.order_tax()}"))
    )
    receipt_list.append(list(("Total items in the order", "", len(order))))

    make_receipt(receipt_list)


if __name__ == "__main__":
    main()
