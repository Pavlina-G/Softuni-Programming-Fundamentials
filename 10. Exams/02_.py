def numbers(num):
    command = input()
    while command != "Finish":
        info = command.split(" ")
        action = info[0]

        if action == "Add":
            value = int(info[1])
            num.append(value)
        elif action == "Remove":
            value = int(info[1])
            if value in num:
                index = num.index(value)
                num.pop(index)
        elif action == "Replace":
            value = int(info[1])
            replacement = int(info[2])
            if value in num:
                index = num.index(value)
                num.insert(index, replacement)
                num.pop(index + 1)
        elif action == "Collapse":
            value = int(info[1])
            num = [x for x in num if x >= value]

        command = input()
    print(*num, sep=" ")


number_list = list(map(int, input().split(" ")))
numbers(number_list)
