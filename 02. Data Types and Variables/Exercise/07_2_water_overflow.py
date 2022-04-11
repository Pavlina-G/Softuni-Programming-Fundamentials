capacity = 0
lines = int(input())

for i in range(lines):
    liters_of_water = int(input())

    if capacity + liters_of_water <+ 255:
        capacity += liters_of_water
        continue

    print("Insufficient capacity!")

print(capacity)

