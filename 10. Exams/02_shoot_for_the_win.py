targets = list(map(int,input().split(" ")))
command = input()
counter = 0

while True:
    if command == "End":
        print(f"Shot targets: {counter} -> {' '.join(map(str, targets))}")
        break

    index = int(command)

    if index in range(len(targets)):
        value = targets[index]
        if targets[index] != -1:
            targets[index] = -1
            counter += 1
            for i in range(len(targets)):
                if targets[i] != -1:
                    if targets[i] > value:
                        targets[i] -= value
                    else:
                        targets[i] += value

    command = input()
