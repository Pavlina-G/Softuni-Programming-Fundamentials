def average_types(dragons_dict, average_dict):
    for types, values in dragons_dict.items():
        count = 0
        for name, value in values.items():
            count += 1
            if types not in average_dict:
                average_dict[types] = [value[0], value[1], value[2]]
            else:
                average_dict[types][0] += value[0]
                average_dict[types][1] += value[1]
                average_dict[types][2] += value[2]
        average_dict[types] = [(average_dict[types][0] / count), (average_dict[types][1] / count), (average_dict[types][2] / count)]

    return average_dict


def dragons():
    dragons_dict = {}
    average_dict = {}

    n = int(input())
    for _ in range(n):
        command = input()
        line = command.split(" ")

        type_dragon, name = line[0], line[1]
        if line[2] != 'null':
            damage = int(line[2])
        else:
            damage = 45
        if line[3] != 'null':
            health = int(line[3])
        else:
            health = 250
        if line[4] != 'null':
            armor = int(line[4])
        else:
            armor = 10

        if type_dragon not in dragons_dict:
            dragons_dict[type_dragon] = {name: [damage, health, armor]}
        else:
            if name in dragons_dict[type_dragon]:
                dragons_dict[type_dragon][name] = [damage, health, armor]
            else:
                dragons_dict[type_dragon][name] = [damage, health, armor]

    average_dict = average_types(dragons_dict, average_dict)

    for t, values in dragons_dict.items():
        for types, average in average_dict.items():
            if t == types:
                print(f"{t}::({average[0]:.2f}/{average[1]:.2f}/{average[2]:.2f})")
        for name, value in sorted(values.items(), key=lambda x: x[0]):
            print(f"-{name} -> damage: {value[0]}, health: {value[1]}, armor: {value[2]}")


dragons()