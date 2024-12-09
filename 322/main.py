# # def process_sales_data(sales_data):
# #     guest_orders = {}
# #     dishes_set = set()
# #     for guest, dish, count in sales_data:
# #         dishes_set.add(dish)
# #     if guest not in guest_orders:
# #         guest_orders[guest] = {}
# #     if dish in guest_orders[guest]:
# #         guest_orders[guest][dish] += count
# #     else:
# #         guest_orders[guest][dish] = count
# #     sorted_guests = sorted(guest_orders.keys())
# #     for guest in sorted_guests:
# #         print(f"{guest}:")
# #     guest_dishes_set = set(guest_orders[guest].keys())
# #
# #     for dish in sorted(guest_dishes_set):
# #         print(f" {dish}: {guest_orders[guest][dish]}")
# #
# #     print()
#
#
# #
# # sales_data = [
# #             ("Alice", "Burger", 2),
# #             ("Eve", "Pizza", 1),
# #             ("Charlie", "Pizza", 3),
# #             ("David", "Burger", 1),
# #             ("Eve", "Salad", 2),
# #         ]
# #
# # process_sales_data(sales_data)
#
#

def process_sales(sales_data):

    guest_orders = {}
    dish_counts = {}

    for sale in sales_data:
        guest, dish, count = sale.split(',')
        guest = guest.strip()
        dish = dish.strip()
        count = int(count.strip())

        if guest not in guest_orders:
            guest_orders[guest] = set()
        guest_orders[guest].add(dish)

        if dish not in dish_counts:
            dish_counts[dish] = 0

        if dish_counts[dish] == 0:
            dish_counts[dish] = count

    sorted_guests = sorted(guest_orders.keys())

    for guest in sorted_guests:
        print(f"{guest}:")
        dishes = sorted(list(guest_orders[guest]))
        for dish in dishes:
            print(f"  {dish}: {dish_counts.get(dish, 0)}\n")

sales_data = [
             ("Alice, Burger, 2"),
             ("Eve, Pizza, 1"),
             ("Charlie, Pizza, 1"),
             ("David, Cola, 1"),
             ("Eve, Salad, 2"),
         ]

process_sales(sales_data)







# n = int(input())
# count=[]
# for i in range(n):
#     set_a = dict(zip(input("Name"),input("Dish")))
#     count.append(input("Count"))
