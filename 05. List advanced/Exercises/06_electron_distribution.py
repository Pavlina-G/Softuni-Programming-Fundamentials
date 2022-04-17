def electron_distribution(num):
    start_position = 1
    electron_list = []

    while True:
        current_position = 2 * start_position ** 2
        start_position += 1
        if num > current_position:
            num -= current_position
            electron_list.append(current_position)
        else:
            electron_list.append(num)
            break

    print(electron_list)

electrons_number = int(input())
electron_distribution(electrons_number)