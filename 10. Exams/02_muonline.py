health = 100
bitcoins = 0
rooms = input().split("|")
counter = 0
condition = False

for room in rooms:
    counter += 1
    info = room.split(" ")
    value = int(info[1])
    action = info[0]

    if action == "potion":
        if health + value <= 100:
            health += value
        else:
            value = 100 - health
            health = 100
        print(f"You healed for {value} hp.")
        print(f"Current health: {health} hp.")
    elif action == "chest":
        print(f"You found {value} bitcoins.")
        bitcoins += value
    else:
        health -= value
        if health > 0:
            print(f"You slayed {action}.")
        else:
            print(f"You died! Killed by {action}.")
            print(f"Best room: {counter}")
            condition = True
            break

if not condition:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")