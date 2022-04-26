def print_func(item, legendary_items, junk_items):
    if item == "shards":
        print("Shadowmourne obtained!")
    elif item == "fragments":
        print("Valanyr obtained!")
    elif item == "motes":
        print("Dragonwrath obtained!")

    print(f"shards: {legendary_items['shards']}")
    print(f"fragments: {legendary_items['fragments']}")
    print(f"motes: {legendary_items['motes']}")

    for items, value in junk_items.items():
        print(f"{items}: {value}")


items_dict = {}
legendary_items = {'shards': 0, "fragments": 0, "motes": 0}
junk_items = {}
condition = False

while True:
    lines = input().lower()
    lines = lines.split(" ")


    for value, item in zip(lines[0::2], lines[1::2]):
        if item in "shards" "fragments" "motes":
            if item not in legendary_items:
                legendary_items[item] = 0

            legendary_items[item] += int(value)

            if legendary_items[item] >= 250:
                legendary_items[item] -= 250
                print_func(item, legendary_items, junk_items)
                condition = True
                break
        if condition:
            break

        if item not in "shards" "fragments" "motes":
            if item not in junk_items:
                junk_items[item] = 0
            junk_items[item] += int(value)

    if condition:
        break
