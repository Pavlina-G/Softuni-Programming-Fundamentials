targets_dict = {}

while True:
    command = input().split("||")
    if command[0] == "Sail":
        break

    city = command[0]
    population = int(command[1])
    gold = int(command[2])

    if city not in targets_dict:
        targets_dict[city] = [population, gold]
    else:
        targets_dict[city][0] += population
        targets_dict[city][1] += gold

while True:
    event = input().split("=>")

    if event[0] == "End":
        if len(targets_dict) == 0:
            print("Ahoy, Captain! All targets have been plundered and destroyed!")
        else:
            print(f"Ahoy, Captain! There are {len(targets_dict)} wealthy settlements to go to:")
            for town, values in targets_dict.items():
                print(f"{town} -> Population: {values[0]} citizens, Gold: {values[1]} kg")

        break

    town = event[1]

    if event[0] == "Plunder":
        people = int(event[2])
        gold = int(event[3])

        if targets_dict[town][0] - people < 0:
            people -= targets_dict[town][0]
            targets_dict[town][0] -= people
        else:
            targets_dict[town][0] -= people

        if targets_dict[town][1] - gold < 0:
            gold -= targets_dict[town][1]
            targets_dict[town][1] -= gold
        else:
            targets_dict[town][1] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if targets_dict[town][0] == 0 or targets_dict[town][1] == 0:
            targets_dict.pop(town)
            print(f"{town} has been wiped off the map!")

    elif event[0] == "Prosper":
        gold = int(event[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            targets_dict[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {targets_dict[town][1]} gold.")
