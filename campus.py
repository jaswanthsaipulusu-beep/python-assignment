
import math

# Route: passenger demand
routes = {
    "Route A": 135,
    "Route B": 90,
    "Route C": 215,
    "Route D": 45
}

bus_capacity = 50
available_buses = 10

total_buses_needed = 0
total_passengers = 0
total_served = 0
total_unserved = 0

print("===== CAMPUS TRANSPORT ALLOCATION =====")

for route, demand in routes.items():
    if demand < 0:
        raise ValueError("Passenger demand cannot be negative.")

    # Minimum buses required for this route
    buses_needed = math.ceil(demand / bus_capacity)
    total_buses_needed += buses_needed
    total_passengers += demand

    # Allocate only the buses still available
    buses_allocated = min(buses_needed, available_buses)
    available_buses -= buses_allocated

    # Passengers served and left unserved
    capacity_provided = buses_allocated * bus_capacity
    passengers_served = min(demand, capacity_provided)
    passengers_unserved = demand - passengers_served

    total_served += passengers_served
    total_unserved += passengers_unserved

    print(f"\n{route}")
    print(f"Passenger demand: {demand}")
    print(f"Buses required: {buses_needed}")
    print(f"Buses allocated: {buses_allocated}")
    print(f"Passengers served: {passengers_served}")
    print(f"Passengers unserved: {passengers_unserved}")

print("\n===== FINAL SUMMARY =====")
print("Total passengers:", total_passengers)
print("Total buses required:", total_buses_needed)
print("Buses available initially:", 10)
print("Buses remaining:", available_buses)
print("Passengers served:", total_served)
print("Passengers unserved:", total_unserved)
