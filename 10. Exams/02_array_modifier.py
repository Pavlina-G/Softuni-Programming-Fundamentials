numbers = list(map(int,input().split(" ")))
command = input()

while command != "end":
    info = command.split(" ")
    action = info[0]
    if command != "decrease":
        index1 = int(info[1])
        index2 = int(info[2])

    if action == "swap":
        numbers[index1],numbers[index2] = numbers[index2],numbers[index1]
    elif action == "multiply":
        result = numbers[index1] * numbers[index2]
        numbers[index1] = result
    elif action == "decrease":
        numbers = list(map(lambda x: x - 1,numbers))

    command = input()

# numbers = list(map(str, numbers))
# print(", ".join(numbers))
print(*numbers,sep=", ")