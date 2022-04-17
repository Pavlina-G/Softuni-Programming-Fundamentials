numbers = list(map(int, input().split(" ")))
commands = input().split(" ")

while commands[0] != "end":

    if commands[0] == "exchange":
        index = int(commands[1])
        if index < 0 or index > (len(numbers) - 1):
            print("Invalid index")
        else:
            first_half = numbers[:index + 1]
            numbers = numbers[index + 1:] + first_half

    elif commands[0] == "max" or commands[0] == "min":
        even_list = list(filter(lambda x: x % 2 == 0, numbers))
        odd_list = list(filter(lambda x: x % 2 != 0, numbers))
        if commands[1] == "even":
            if len(even_list) == 0:
                print("No matches")
            else:
                if commands[0] == "max" and commands[1] == "even":
                    # prints the rightmost index of more than 1 max value
                    print(len(numbers) - 1 - numbers[::-1].index((max(even_list))))
                elif commands[0] == "min" and commands[1] == "even":
                    print(len(numbers) - 1 - numbers[::-1].index(min(even_list)))

        elif commands[1] == "odd":
            if len(odd_list) == 0:
                print("No matches")
            else:
                if commands[0] == "max" and commands[1] == "odd":
                    print(len(numbers) - 1 - numbers[::-1].index(max(odd_list)))
                elif commands[0] == "min" and commands[1] == "odd":
                    print(len(numbers) - 1 - numbers[::-1].index(min(odd_list)))

    elif commands[0] == "first" or commands[0] == "last":
        even_list = list(filter(lambda x: x % 2 == 0, numbers))
        odd_list = list(filter(lambda x: x % 2 != 0, numbers))
        count = int(commands[1])

        if count > len(numbers):
            print("Invalid count")
        else:

            if commands[2] == "even":
                if commands[0] == "first":
                    print(even_list[:count])
                elif commands[0] == "last":
                    print(even_list[-count:])
            elif commands[2] == "odd":
                if commands[0] == "first":
                    print(odd_list[:count])
                elif commands[0] == "last":
                    print(odd_list[-count:])

    commands = input().split(" ")

print(numbers)
