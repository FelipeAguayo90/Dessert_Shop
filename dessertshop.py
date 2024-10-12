import dessert as d


def main():
    new_oder = d.Order()
    new_oder.add(d.Candy("Candy Corn", 1.5, 0.25))
    new_oder.add(d.Candy("Gummy Bears", 0.25, 0.35))
    new_oder.add(d.Cookie("Chocolate Chip", 6, 3.99))
    new_oder.add(d.IceCream("Pistachio", 2, 0.79))
    new_oder.add(d.Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29))
    new_oder.add(d.Cookie("Oatmeal Raisin", 2, 3.45))
    print(new_oder)


if __name__ == "__main__":
    main()
