targets = list(map(int, input().split(" ")))
command = input()

while command != "End":
    info = command.split(" ")
    action = info[0]
    index = int(info[1])
    value = int(info[2])
    
    if action == "Shoot":
        if index in range(len(targets)):
            if targets[index] - value > 0:
                targets[index] -= value
            else:
                targets.pop(index)
    elif action == "Add":
        if index in range(len(targets)):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        if (index - value) in range(len(targets)) and (index + value) in range(len(targets)):
            targets = targets[:index - value] + targets[index + value + 1:]
        else:
            print("Strike missed!")

    command = input()

print(*targets, sep="|")
