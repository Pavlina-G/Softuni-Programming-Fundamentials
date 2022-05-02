initial_loot = input().split("|")
command = input()

while command != "Yohoho!":
    info = command.split(" ")
    action = info[0]

    if action == "Loot":
        for item in range(1, len(info)):
            if info[item] not in initial_loot:
                initial_loot.insert(0, info[item])

    elif action == "Drop":
        index_drop = int(info[1])
        if index_drop in range(len(initial_loot)):
            item = initial_loot[index_drop]
            initial_loot.pop(index_drop)
            initial_loot.append(item)

    elif action == "Steal":
        count = int(info[1])
        if count in range(len(initial_loot)):
            stolen_items = initial_loot[-count:]
            initial_loot = initial_loot[:-count]
        else:
            stolen_items = initial_loot
            initial_loot = []
        print(", ".join(stolen_items))

    command = input()

if len(initial_loot) == 0:
    print("Failed treasure hunt.")
else:
    average = 0
    for x in initial_loot:
        average += len(x)
    average = average / len(initial_loot)
    print(f"Average treasure gain: {average:.2f} pirate credits.")

