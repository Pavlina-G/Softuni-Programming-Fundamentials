fire_cells = input().split("#")
water_amount = int(input())
effort = 0
total_fire = 0

print(f"Cells:")

for fire in fire_cells:
    condition = False

    fire_info = fire.split(' = ')
    type_of_fire = fire_info[0]
    cell_level = int(fire_info[1])

    if type_of_fire == "High":
        if 81 <= cell_level <= 125:
            condition = True
    elif type_of_fire == "Medium":
        if 51 <= cell_level <= 80:
            condition = True
    elif type_of_fire == "Low":
        if 1 <= cell_level <= 50:
            condition = True

    if condition:
        if water_amount >= cell_level:
            water_amount -= cell_level
            total_fire += cell_level
            effort += 0.25 * cell_level
            print(f" - {cell_level}")


print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")


