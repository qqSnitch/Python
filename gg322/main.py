def process_sales_data(sales_data):
    guest_orders = {}
    dishes_set = set()

    for guest, dish, quantity in sales_data:
        dishes_set.add(dish)

        if guest not in guest_orders:
            guest_orders[guest] = {}

        if dish in guest_orders[guest]:
            guest_orders[guest][dish] += quantity
        else:
            guest_orders[guest][dish] = quantity

    sorted_guests = sorted(guest_orders.keys())

    for guest in sorted_guests:
        print(f"{guest}:")

        guest_dishes_set = set(guest_orders[guest].keys())

        for dish in sorted(guest_dishes_set):
            print(f" {dish}: {guest_orders[guest][dish]}")

        print()

sales_data = [
    ("Alice", "Burger", 2),
    ("Bob", "Salad", 1),
    ("Eve", "Pizza", 3),
    ("David", "Burger", 1),
    ("Eve", "Salad", 2),
    ("Eve", "Salad", 2),
    ]

process_sales_data(sales_data)