
expenses = [
    [[12000, 8000, 5000],
     [13000, 7500, 5500],
     [12500, 8200, 4800]],

    [[15000, 9000, 6000],
     [14500, 9500, 6500],
     [16000, 9200, 6200]],

    [[10000, 7000, 4000],
     [11000, 7200, 4500],
     [10500, 6800, 4300]]
]

branches = ["Branch 1", "Branch 2", "Branch 3"]
categories = ["Salaries", "Rent", "Utilities"]
months = ["January", "February", "March"]

grand_total = 0
category_totals = [0] * len(categories)
branch_totals = []

for b, branch in enumerate(expenses):
    branch_total = 0

    for m, month in enumerate(branch):
        monthly_total = sum(month)
        branch_total += monthly_total

        print(f"{branches[b]} - {months[m]}: "
              f"₹{monthly_total:,}")

        for c, amount in enumerate(month):
            category_totals[c] += amount

    branch_totals.append(branch_total)
    grand_total += branch_total

print("\n--- Branch Analysis ---")

for i, total in enumerate(branch_totals):
    average = total / len(months)
    print(f"{branches[i]}: Total ₹{total:,}, "
          f"Monthly Average ₹{average:,.2f}")

print("\n--- Category Analysis ---")

for i, total in enumerate(category_totals):
    print(f"{categories[i]}: ₹{total:,}")

print(f"\nGrand Total: ₹{grand_total:,}")
print(f"Overall Monthly Average: "
      f"₹{grand_total / len(months):,.2f}")

largest_branch = branches[branch_totals.index(max(branch_totals))]
largest_category = categories[
    category_totals.index(max(category_totals))
]

print(f"Largest Spending Branch: {largest_branch}")
print(f"Largest Expense Category: {largest_category}")
