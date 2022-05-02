elements = input().split(" ")

command = input()
moves = 0

while True:
    if command == "end":
        break

    info = command.split(" ")
    index1 = int(info[0])
    index2 = int(info[1])
    moves += 1

    if len(elements) > 0:
        if index1 == index2 or index1 >= len(elements) or index2 >= len(elements) or index1 < 0 or index2 < 0:
            print("Invalid input! Adding additional elements to the board")
            elements.insert(len(elements)//2,f"-{moves}a")
            elements.insert(len(elements)//2,f"-{moves}a")

        elif elements[index1] == elements[index2]:
            del_element = elements[index1]
            print(f"Congrats! You have found matching elements - {elements[index1]}!")
            elements = list(filter(lambda a: a != del_element, elements))

        elif elements[index1] != elements[index2]:
            print("Try again!")

    if len(elements) == 0:
        break

    command = input()

if len(elements) == 0:
    print(f"You have won in {moves} turns!")
if len(elements) > 0:
    print("Sorry you lose :(")
    print(" ".join(elements))


