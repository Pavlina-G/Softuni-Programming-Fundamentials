import re

password = input()

while True:
    command = input()
    if command == "Complete":
        break
    info = command.split(' ')

    if info[0] == 'Make':
        index = int(info[2])

        if info[1] == "Upper":
            letter = password[index].upper()
            password = password[:index] + letter + password[index + 1:]
            print(password)

        elif info[1] == "Lower":
            letter = password[index].lower()
            password = password[:index] + letter + password[index + 1:]
            print(password)

    elif info[0] == "Insert":
        index = int(info[1])
        char = info[2]
        if index in range(len(password)):
            password = password[:index] + char + password[index:]
            print(password)

    elif info[0] == "Replace":
        char = info[1]
        value = int(info[2])
        if char in password:
            char_value = ord(char) + value
            password = password.replace(char, chr(char_value))
            print(password)

    elif info[0] == "Validation":
        condition = password.isalnum() or '_' in password
        if len(password) < 8:
            print("Password must be at least 8 characters long!")
        if not condition:
            print("Password must consist only of letters, digits and _!")
        if not any(char.isupper() for char in password):
            print("Password must consist at least one uppercase letter!")
        if not any(char.islower() for char in password):
            print("Password must consist at least one lowercase letter!")
        if not any(char.isdigit() for char in password):
            print("Password must consist at least one digit!")
