
transactions = [
    ("T101", 5000, "CREDIT"),
    ("T102", 2000, "DEBIT"),
    ("T103", -500, "DEBIT"),
    ("T102", 1500, "CREDIT"),
    ("T104", 0, "DEBIT"),
    ("T105", 90000, "DEBIT"),
    ("T106", 1000, "CREDIT"),
    ("T107", 95000, "DEBIT"),
    ("T108", 500, "TRANSFER"),
    ("T109", 3000, "CREDIT")
]

seen_ids = set()
duplicates = []
invalid_amounts = []
suspicious_sequences = []

# Audit each transaction
for i, (tid, amount, ttype) in enumerate(transactions):

    # 1. Detect duplicate identifiers
    if tid in seen_ids:
        duplicates.append(tid)
    else:
        seen_ids.add(tid)

    # 2. Detect invalid amounts and types
    if (not isinstance(amount, (int, float))
            or isinstance(amount, bool)
            or amount <= 0):
        invalid_amounts.append((tid, amount))

    if ttype not in ("CREDIT", "DEBIT", "TRANSFER"):
        invalid_amounts.append((tid, "Invalid transaction type"))

    # 3. Detect consecutive high-value debits
    if i > 0:
        prev_id, prev_amount, prev_type = transactions[i - 1]

        if (isinstance(amount, (int, float))
                and not isinstance(amount, bool)
                and isinstance(prev_amount, (int, float))
                and not isinstance(prev_amount, bool)
                and amount >= 50000
                and prev_amount >= 50000
                and amount > 0
                and prev_amount > 0
                and ttype == "DEBIT"
                and prev_type == "DEBIT"):
            suspicious_sequences.append(
                (prev_id, tid, prev_amount, amount)
            )

# Print audit report
print("=== TRANSACTION AUDIT REPORT ===")

print("\nDuplicate Transaction IDs:")
print(duplicates if duplicates else "None")

print("\nInvalid Amounts or Transaction Types:")
print(invalid_amounts if invalid_amounts else "None")

print("\nSuspicious Consecutive High-Value Debits:")
print(suspicious_sequences if suspicious_sequences else "None")

print("\nTotal Transactions:", len(transactions))
print("Unique Transaction IDs:", len(seen_ids))
