def menu():
    menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    return menu


def main():
    items_menu = menu()

    total_cost = 0.00

    while True:
        try:
            item = input("Item: ").title()
        except EOFError:
            break

        if item not in items_menu:
            continue

        total_cost += items_menu[item]
        print(f"${total_cost:.2f}")

    print()
    print(f"Total Cost: ${total_cost:.2f}")

main()