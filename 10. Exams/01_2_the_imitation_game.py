message = input()

while True:
    command = input().split('|')

    if command[0] == "Decode":
        break

    if command[0] == "Move":
        number = int(command[1])
        message = message[number:] + message[:number]

    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        message = message[:index] + value + message[index:]

    elif command[0] == "ChangeAll":
        old_string = command[1]
        new_string = command[2]
        message = message.replace(old_string, new_string)

print(f"The decrypted message is: {message}")