gifts = input().split(' ')
commands = input()

while commands != "No Money":
    commands_split = commands.split(' ')
    command = commands_split[0]
    gift = commands_split[1]

    if command == "OutOfStock":
        for i,value in enumerate(gifts):
            if value == gift:
                gifts[i] = 'None'

    elif command == "Required":
        command_index = int(commands_split[2])
        if 0 <= command_index < len(gifts):
            gifts[command_index] = gift

    elif command == "JustInCase":
        gifts[-1] = gift

    commands = input()

while "None" in gifts:
    gifts.remove("None")

print(' '.join(gifts))