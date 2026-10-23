# 1. Setup the bus parameters
MAX_CAPACITY = 40
current_passengers = 0

# 2. Define the route data (Stop Name, People Getting Off, People Getting On)
stops = [
    ("Central Station", 0, 25),
    ("Financial District", 5, 18),
    ("University Quad", 12, 20),
    ("Shopping Mall", 22, 5),
    ("Suburban Terminal", 29, 0)
]

print(f"Bus Simulation Started (Max Capacity: {MAX_CAPACITY})\n")

# 3. Loop through each stop sequentially
for name, alighted, boarded in stops:

    # Safety Check: Can't have more people get off than are on the bus
    if alighted > current_passengers:
        alighted = current_passengers

    # Update the headcount
    current_passengers = current_passengers - alighted + boarded

    # Print the current status
    print(f"Stop: {name}")
    print(f"  -> Off: {alighted} | On: {boarded} | Total inside bus: {current_passengers}")

    # Check if the bus is overcrowded
    if current_passengers > MAX_CAPACITY:
        excess = current_passengers - MAX_CAPACITY
        print(f"  🚨 WARNING: Over capacity by {excess} passenger(s)!")

    print("-" * 40)

print("\nRoute Completed!")
