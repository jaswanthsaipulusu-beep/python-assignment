
# Initial inventory: item -> [price, quantity]
inventory = {
    "Idli": [30, 50],
    "Dosa": [50, 30],
    "Meals": [80, 20],
    "Tea": [10, 100],
    "Samosa": [15, 40]
}

daily_sales = 0
successful_orders = 0
rejected_orders = 0
sales_by_item = {item: 0 for item in inventory}

# Successive customer orders
orders = [
    {"Idli": 2, "Tea": 2},
    {"Dosa": 1, "Samosa": 3},
    {"Meals": 2, "Tea": 1},
    {"Dosa": 50},       # Rejected: insufficient stock
    {"Tea": 5, "Idli": 1}
]

for order_no, order in enumerate(orders, start=1):
    print(f"\nCustomer Order {order_no}")
    valid = True

    # Validate the entire order before updating stock
    for item, qty in order.items():
        if item not in inventory:
            print(f"Rejected: {item} is unavailable.")
            valid = False
            break

        if (not isinstance(qty, int) or isinstance(qty, bool)
                or qty <= 0):
            print(f"Rejected: Invalid quantity for {item}.")
            valid = False
            break

        if qty > inventory[item][1]:
            print(f"Rejected: Only {inventory[item][1]} "
                  f"{item}(s) available.")
            valid = False
            break

    if not valid:
        rejected_orders += 1
        continue

    # Calculate bill and update stock
    bill = 0

    for item, qty in order.items():
        price = inventory[item][0]
        bill += price * qty

    for item, qty in order.items():
        inventory[item][1] -= qty
        sales_by_item[item] += qty

    daily_sales += bill
    successful_orders += 1

    print("Items:", order)
    print(f"Total Bill: Rs. {bill}")

# Daily summary
print("\n===== DAILY SALES REPORT =====")
print(f"Successful Orders: {successful_orders}")
print(f"Rejected Orders: {rejected_orders}")
print(f"Total Sales: Rs. {daily_sales}")

print("\nItems Sold:")
for item, qty in sales_by_item.items():
    if qty > 0:
        print(f"{item}: {qty}")

print("\nRemaining Inventory:")
for item, (price, stock) in inventory.items():
    print(f"{item}: {stock} units")
