def targets(shots):
    command = input()

    while command != "End":
        info = command.split()
        action = info[0]
        index = int(info[1])
        value = int(info[2])

        if action == "Shoot":
            if index in range(len(shots)):
                if shots[index] - value > 0:
                    shots[index] -= value
                else:
                    shots.pop(index)
        elif action == "Add":
            if index in range(len(shots)):
                shots.insert(index, value)
            else:
                print("Invalid placement!")

        elif action == "Strike":
            if (index - value) in range(len(shots)) and (index + value) in range(len(shots)):
                value_del = list(shots[index - value:index + value + 1])
                for i in value_del:
                    shots.remove(i)
            else:
                print("Strike missed!")

        command = input()

    print(*shots,sep="|")


sequence_of_targets = list(map(int, input().split(" ")))
targets(sequence_of_targets)
