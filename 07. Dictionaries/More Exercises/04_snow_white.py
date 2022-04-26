items = input()
dwarfs = {}
colors = {}
while items != "Once upon a time":
    info = items.split(" <:> ")
    name = info[0]
    color = info[1]
    physics = int(info[2])
    id = name + ":" + color
    if id not in dwarfs:
        if color not in colors:
            colors[color] = 1
        else:
            colors[color] += 1
        dwarfs[id] = [0, color]

    dwarfs[id][0] = max([dwarfs[id][0], physics])
    items = input()

sorted_dwrafs = dict(sorted(dwarfs.items(), key=lambda x: (x[1][0], colors[x[1][1]]), reverse=True))

for key, value in sorted_dwrafs.items():
    info = key.split(":")

    print(f"({info[1]}) {info[0]} <-> {value[0]}")