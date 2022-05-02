stops = input()

while True:
    command = input()
    if command == "Travel":
        break

    command = command.split(':')
    if command[0] == 'Add Stop':
        index = int(command[1])
        new_string = command[2]
        if index in range(len(stops)):
            stops = stops[:index] + new_string + stops[index:]
        print(stops)

    elif command[0] == 'Remove Stop':
        start_index = int(command[1])
        end_index = int(command[2])

        if start_index in range(len(stops)) and end_index in range(len(stops)):
            stops = stops[:start_index] + stops[end_index + 1:]
        print(stops)

    elif command[0] == 'Switch':
        old_str = command[1]
        new_str = command[2]
        if old_str in stops:
            stops = stops.replace(old_str, new_str)
        print(stops)

print(f"Ready for world tour! Planned stops: {stops}")
