class FoodWasteMonitor:
    def __init__(self, location_id: str, acceptable_waste_pct: float = 10.0):
        """
        Initializes the food waste audit metrics.
        """
        self.location_id = location_id
        self.acceptable_waste_pct = acceptable_waste_pct
        self.audit_log = []
        self.threshold_violations = []

    def process_daily_metrics(self, tracking_data: list):
        """
        Processes kitchen logs across multiple days.
        Calculates volumetric metrics and evaluates operational waste compliance.
        """
        print(f"=== Starting Food Waste Audit for: {self.location_id} ===")
        print(f"Acceptable Waste Limit: {self.acceptable_waste_pct}%\n")

        # Header formatting for the real-time daily metrics table
        print(
            f"{'Date/Day':<12} | {'Prepared (kg)':<14} | {'Served (kg)':<12} | {'Leftovers (kg)':<14} | {'Waste %':<10} | {'Status':<12}")
        print("-" * 85)

        for day in tracking_data:
            date = day["date"]
            prepared = day["prepared_meals_kg"]
            served = day["meals_served_kg"]
            leftovers = day["leftovers_kg"]

            # 1. Verification Logic Check
            # Prepared meals must equal served meals plus leftover baseline structures.
            # If a data mismatch occurs, we isolate the discrepancy as direct unserved kitchen waste.
            accounted_food = served + leftovers
            unexplained_loss = prepared - accounted_food

            # Total waste volume equals measured leftovers plus unexplained technical storage shrinkage
            total_waste = leftovers + max(0, unexplained_loss)

            # 2. Percentage Calculation
            # Protect against ZeroDivisionError if zero meals were prepared on a holiday
            waste_percentage = 0.0
            if prepared > 0:
                waste_percentage = round((total_waste / prepared) * 100, 2)

            # 3. Compliance Checking
            status = "COMPLIANT"
            if waste_percentage > self.acceptable_waste_pct:
                status = "🚨 EXCEEDED"
                self.threshold_violations.append({
                    "date": date,
                    "waste_pct": waste_percentage,
                    "excess_pct": round(waste_percentage - self.acceptable_waste_pct, 2)
                })

            # Save historical records
            self.audit_log.append({
                "date": date,
                "prepared": prepared,
                "served": served,
                "leftovers": leftovers,
                "waste_pct": waste_percentage
            })

            # Print day analytics
            print(
                f"{date:<12} | {prepared:<14} | {served:<12} | {leftovers:<14} | {waste_percentage:<10}% | {status:<12}")

        print("-" * 85)
        self._generate_sustainability_report()

    def _generate_sustainability_report(self):
        """
        Aggregates compiled records to output a centralized facility analysis.
        """
        total_prepared = sum(d["prepared"] for d in self.audit_log)
        total_waste = sum(d["leftovers"] for d in self.audit_log)

        avg_waste_pct = round((total_waste / total_prepared) * 100, 2) if total_prepared > 0 else 0.0

        print("\n=== SUSTAINABILITY AUDIT REPORT ===")
        print(f"Total Food Volume Processed: {total_prepared} kg")
        print(f"Cumulative Facility Waste:    {total_waste} kg")
        print(f"Average Period Waste Factor:  {avg_waste_pct}%")

        if self.threshold_violations:
            print(f"\n⚠️ CRITICAL: {len(self.threshold_violations)} non-compliant instances identified.")
            for violation in self.threshold_violations:
                print(f"  - On {violation['date']}: Waste limit reached {violation['waste_pct']}% "
                      f"({violation['excess_pct']}% above target zone!)")
        else:
            print("\n✅ Environmental Performance Check: All days maintained compliant waste parameters.")
        print("===================================\n")


# --- Execution Example ---
if __name__ == "__main__":
    # Operational metrics tracked over a regular working week (mass in kilograms)
    weekly_kitchen_data = [
        {"date": "Monday", "prepared_meals_kg": 150, "meals_served_kg": 140, "leftovers_kg": 10},  # 6.67% (OK)
        {"date": "Tuesday", "prepared_meals_kg": 160, "meals_served_kg": 135, "leftovers_kg": 25},  # 15.63% (Exceeds!)
        {"date": "Wednesday", "prepared_meals_kg": 140, "meals_served_kg": 132, "leftovers_kg": 8},  # 5.71% (OK)
        {"date": "Thursday", "prepared_meals_kg": 170, "meals_served_kg": 145, "leftovers_kg": 25},  # 14.71% (Exceeds!)
        {"date": "Friday", "prepared_meals_kg": 180, "meals_served_kg": 172, "leftovers_kg": 8}  # 4.44% (OK)
    ]

    # Initialize monitoring stack: Flag any days exceeding a strict 10% structural waste limit
    monitor = FoodWasteMonitor(location_id="Central Cafeteria HQ", acceptable_waste_pct=10.0)
    monitor.process_daily_metrics(weekly_kitchen_data)
