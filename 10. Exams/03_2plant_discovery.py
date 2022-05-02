n = int(input())
plants_dict = {}

for i in range(n):
    line = input().split('<->')
    plant = line[0]
    rarity = int(line[1])

    if plant not in plants_dict:
        plants_dict[plant] = {}
        plants_dict[plant]['Rarity'] = [rarity]
        plants_dict[plant]['Rating'] = []

    else:
        plants_dict[plant]['Rarity'] = [rarity]

command = input()
while command != "Exhibition":
    command = command.split(':')
    info = command[1].split(' - ')
    plant_info = info[0].strip()

    if plant_info in plants_dict:

        if command[0] == 'Rate':
            rating = int(info[1])
            plants_dict[plant_info]['Rating'].append(rating)

        elif command[0] == 'Update':
            new_rarity = int(info[1])
            if plant_info in plants_dict:
                plants_dict[plant_info]['Rarity'] = [new_rarity]

        elif command[0] == 'Reset':
            if plant_info in plants_dict:
                plants_dict[plant_info]['Rating'] = []

        else:
            print(f"error")
    else:
        print(f"error")

    command = input()

print(f"Plants for the exhibition:")

for key, value in plants_dict.items():

    if len(value['Rating']) > 0:
        print(f"- {key}; Rarity: {sum(value['Rarity'])}; Rating: {sum(value['Rating']) / len(value['Rating']):.2f}")
    else:
        print(f"- {key}; Rarity: {sum(value['Rarity'])}; Rating: {sum(value['Rating']):.2f}")