import dessert as d
from receipt import make_receipt


def main():
    new_oder = d.Order()
    new_oder.add(d.Candy("Candy Corn", 1.5, 0.25))
    new_oder.add(d.Candy("Gummy Bears", 0.25, 0.35))
    new_oder.add(d.Cookie("Chocolate Chip", 6, 3.99))
    new_oder.add(d.IceCream("Pistachio", 2, 0.79))
    new_oder.add(d.Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29))
    new_oder.add(d.Cookie("Oatmeal Raisin", 2, 3.45))
    print(new_oder)

    receipt_list = [["Name", "Item Cost", "Tax"]]
    subtotal_cost = 0
    subtotal_tax = 0

    for item in new_oder._oder:
        cost = item.calculate_cost()
        tax = item.calculate_tax()
        subtotal_cost += cost
        subtotal_tax += tax
        receipt_list.append(list((item.name, f"${cost:.2f}", f"${tax:.2f}")))
    receipt_list.append(
        list(
            (
                "Order Subtotals",
                f"${new_oder.order_cost():.2f}",
                f"${new_oder.order_tax():.2f}",
            )
        )
    )
    receipt_list.append(
        list(("Order Total", "", f"${new_oder.order_cost() + new_oder.order_tax()}"))
    )
    receipt_list.append(list(("Total items in the order", "", len(new_oder))))

    make_receipt(receipt_list)


if __name__ == "__main__":
    main()
