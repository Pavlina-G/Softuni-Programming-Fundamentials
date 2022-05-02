stops = input()

command = input()

while command != "Travel":
    info = command.split(":")
    action = info[0]

    if action == "Add Stop":
        index = int(info[1])
        value = info[2]
        if index in range(len(stops)):
            stops = stops[:index] + value + stops[index:]
        print(stops)

    elif action == "Remove Stop":
        start_index = int(info[1])
        end_index = int(info[2])
        if start_index in range(len(stops)) and end_index in range(len(stops)):
            stops = stops[:start_index] + stops[end_index+1:]
        print(stops)
    elif action == "Switch":
        old_string = info[1]
        new_string = info[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)

    command = input()

print(f"Ready for world tour! Planned stops: {stops}")