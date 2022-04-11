capacity = 255
lines = int(input())
total_water = 0

for i in range(1, lines + 1):
    litters_of_water = int(input())

    if capacity - litters_of_water < 0:
        print("Insufficient capacity!")
        continue
    else:
        total_water += litters_of_water
        capacity -= litters_of_water

print(total_water)

