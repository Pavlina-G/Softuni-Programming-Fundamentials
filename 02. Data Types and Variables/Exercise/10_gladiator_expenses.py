lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

fights_counter = 1

total_expense = 0
helmet_counter = 0
sword_counter = 0
shields_counter = 0
armor_counter = 0


while fights_counter <= lost_fights_count:

    if fights_counter % 2 == 0:
        helmet_counter += 1
    if fights_counter % 3 == 0:
        sword_counter += 1
    if fights_counter % 2 == 0 and fights_counter % 3 == 0:
        shields_counter += 1
        if shields_counter % 2 == 0:
            armor_counter += 1

    fights_counter += 1

total_expense = (helmet_price * helmet_counter + sword_price * sword_counter + shield_price * shields_counter + armor_price * armor_counter)
print(f"Gladiator expenses: {total_expense:.2f} aureus")

