
# Borrowing records: (book_id, borrowing_period, return_delay)
# return_delay: 0 means on time; positive means late;
# -1 means the book has not yet been returned.

records = [
    ("B101", 7, 0),
    ("B102", 14, 3),
    ("B103", 7, -1),
    ("B104", 10, 5),
    ("B105", 14, 0),
    ("B106", 7, -1)
]

FINE_PER_DAY = 5

total_fines = 0
overdue_records = []
available_books = set()
borrowed_books = set()
seen_books = set()

print("===== LIBRARY BORROWING REPORT =====")

for book_id, period, delay in records:

    if book_id in seen_books:
        print(f"Duplicate record: {book_id}")
        continue
    seen_books.add(book_id)

    if (not isinstance(period, int) or isinstance(period, bool)
            or period <= 0):
        print(f"Invalid borrowing period: {book_id}")
        continue

    if (not isinstance(delay, int) or isinstance(delay, bool)
            or delay < -1):
        print(f"Invalid return delay: {book_id}")
        continue

    # Book availability and fine calculation
    if delay == -1:
        borrowed_books.add(book_id)
        print(f"{book_id}: Not returned yet")
        continue

    available_books.add(book_id)
    fine = delay * FINE_PER_DAY
    total_fines += fine

    if delay > 0:
        overdue_records.append((book_id, delay, fine))
        print(f"{book_id}: Overdue by {delay} days, "
              f"Fine = Rs. {fine}")
    else:
        print(f"{book_id}: Returned on time, No fine")

print("\n===== FINE RECONCILIATION =====")
print("Total fines due: Rs.", total_fines)
print("Overdue returned books:", len(overdue_records))

for book_id, delay, fine in overdue_records:
    print(f"{book_id}: {delay} days late, Rs. {fine}")

print("\n===== BOOK AVAILABILITY =====")
print("Available books:", sorted(available_books))
print("Currently borrowed books:", sorted(borrowed_books))
print("Available count:", len(available_books))
print("Borrowed count:", len(borrowed_books))
