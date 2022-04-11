from math import floor

group_size = int(input())
days_of_adventure = int(input())
gained_coins = 0
spent_coins = 0

for day in range(1, days_of_adventure + 1):
    motivational_party = False

    gained_coins += 50

    if day % 10 == 0:
        group_size -= 2

    if day % 15 == 0:
        group_size += 5

    spent_coins += 2 * group_size

    if day % 3 == 0:
        spent_coins += 3 * group_size
        motivational_party = True

    if day % 5 == 0:
        gained_coins += 20 * group_size
        if motivational_party:
            spent_coins += 2 * group_size

profit = (gained_coins - spent_coins)/group_size

print(f"{group_size} companions received {int(profit)} coins each.")

