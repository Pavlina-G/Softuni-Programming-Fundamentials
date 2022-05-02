message = input()
command = input()

while command != "Reveal":
    info = command.split(":|:")
    if info[0] == 'InsertSpace':
        index = int(info[1])
        message = message[:index] + ' ' + message[index:]
        print(message)

    elif info[0] == 'Reverse':
        substring = info[1]
        if substring in message:
            start_index = message.find(substring)
            end_index = start_index + len(substring) - 1
            message = message[:start_index] + message[end_index+1:] + ''.join(reversed(substring))
            print(message)
        else:
            print('error')

    elif info[0] == 'ChangeAll':
        sub_string = info[1]
        replacement = info[2]
        message = message.replace(sub_string, replacement)
        print(message)

    command = input()

print(f"You have a new text message: {message}")