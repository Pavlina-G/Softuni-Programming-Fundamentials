bread_count = 0
budget = float(input())
price_per_kg_flour = float(input())
price_for_pack_of_egg = 0.75 * price_per_kg_flour
price_for_milk_250ml = (1.25 * price_per_kg_flour) / 4
price_for_bread = price_for_milk_250ml + price_for_pack_of_egg + price_per_kg_flour
coloured_eggs = 0

while budget > price_for_bread:
    budget -= price_for_bread
    bread_count += 1
    coloured_eggs += 3
    if bread_count % 3 == 0:
        coloured_eggs -= (bread_count - 2)
print(f"You made {bread_count} loaves of Easter bread! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.")

