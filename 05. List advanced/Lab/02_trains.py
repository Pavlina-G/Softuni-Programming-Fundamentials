wagons = int(input())
wagon_list = [0] * wagons

command = input().split(" ")

while command[0] != "End":

    if command[0] == "add":
        wagon_list[-1] += int(command[1])
    elif command[0] == "insert":
        wagon_list[int(command[1])] += int(command[2])
    elif command[0] == "leave":
        wagon_list[int(command[1])] -= int(command[2])

    command = input().split(" ")
print(wagon_list)
