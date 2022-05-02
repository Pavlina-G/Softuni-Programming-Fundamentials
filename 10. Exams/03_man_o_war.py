def fire_func(warship, info):
    index = int(info[1])
    damage = int(info[2])
    if index in range(len(warship)):
        for i in range(len(warship)):
            if i == index:
                warship[i] -= damage
                if warship[i] <= 0:
                    print(f"You won! The enemy ship has sunken.")
                    break
                return warship


def defend_func(ships, info):
    start_index = int(info[1])
    end_index = int(info[2])
    damage = int(info[3])
    if start_index in range(len(ships)) and end_index in range(len(ships)):
        for index in range(start_index, end_index + 1):
            ships[index] -= damage
            if ships[index] <= 0:
                print("You lost! The pirate ship has sunken.")
                break

        return ships


def repair_func(max_health, ship, info):
    index = int(info[1])
    health = int(info[2])
    if index in range(len(ship)):
        ship[index] += health
        if ship[index] > max_health:
            ship[index] = max_health

    return ship


def status_func(ship, max_health):
    repair_list = [int(x) for x in ship if int(x) < max_health * 0.20]
    print(f"{len(repair_list)} sections need repair.")


def man_o_war(ship, warship, max_health):
    while True:
        condition = False
        command = input()
        if command == "Retire":
            break
        info = command.split(" ")
        action = info[0]
        if action == "Fire":
            fire_func(warship, info)
            for x in warship:
                if x <= 0:
                    condition = True
            if condition:
                break
        elif action == "Defend":
            defend_func(ship, info)

            for x in ship:
                if x <= 0:
                    condition = True
            if condition:
                break
        elif action == "Repair":
            repair_func(max_health, ship, info)
        elif action == "Status":
            status_func(ship, max_health)
    if not condition:
        if len(ship) > 0 and len(warship) > 0:
            print(f"Pirate ship status: {sum(ship)}")
            print(f"Warship status: {sum(warship)}")


status_ship = list(map(int, input().split(">")))
status_warship = list(map(int, input().split(">")))
maximum_health = int(input())

man_o_war(status_ship, status_warship, maximum_health)
