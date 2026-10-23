
# Production matrix:
# Product -> Batch -> [units produced, defective units]

production = {
    "Product A": {
        "Batch 101": [1000, 25],
        "Batch 102": [800, 48],
        "Batch 103": [1200, 30]
    },
    "Product B": {
        "Batch 201": [1500, 90],
        "Batch 202": [1000, 20],
        "Batch 203": [900, 63]
    },
    "Product C": {
        "Batch 301": [700, 14],
        "Batch 302": [1100, 66],
        "Batch 303": [600, 18]
    }
}

quality_threshold = 5.0

total_produced = 0
total_defective = 0
failed_batches = []

print("===== MANUFACTURING QUALITY REPORT =====")

for product, batches in production.items():
    print(f"\n{product}")

    product_produced = 0
    product_defective = 0

    for batch, values in batches.items():
        produced, defective = values

        if (not isinstance(produced, int)
                or isinstance(produced, bool)
                or not isinstance(defective, int)
                or isinstance(defective, bool)
                or produced <= 0
                or defective < 0
                or defective > produced):
            raise ValueError(f"Invalid data in {batch}")

        defect_rate = defective / produced * 100

        product_produced += produced
        product_defective += defective
        total_produced += produced
        total_defective += defective

        status = (
            "FAIL" if defect_rate > quality_threshold
            else "PASS"
        )

        print(
            f"{batch}: Produced={produced}, "
            f"Defective={defective}, "
            f"Defect Rate={defect_rate:.2f}%, "
            f"Status={status}"
        )

        if defect_rate > quality_threshold:
            failed_batches.append(
                (product, batch, defect_rate)
            )

    product_rate = product_defective / product_produced * 100

    print(f"{product} Total Produced: {product_produced}")
    print(f"{product} Total Defective: {product_defective}")
    print(f"{product} Defect Rate: {product_rate:.2f}%")

overall_rate = total_defective / total_produced * 100

print("\n===== FINAL QUALITY SUMMARY =====")
print("Total Units Produced:", total_produced)
print("Total Defective Units:", total_defective)
print(f"Overall Defect Rate: {overall_rate:.2f}%")

print("\nBatches Exceeding Quality Threshold:")
if failed_batches:
    for product, batch, rate in failed_batches:
        print(f"{product} - {batch}: {rate:.2f}%")
else:
    print("No batches exceeded the threshold.")
