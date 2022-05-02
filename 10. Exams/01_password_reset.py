def password_reset():
    password = input()

    while True:
        command = input()
        if command == "Done":
            print(f"Your password is: {password}")
            break

        command = command.split(" ")

        if command[0] == "TakeOdd":
            password = ''.join([password[x] for x in range(len(password)) if x % 2 != 0])
            print(password)

        elif command[0] == "Cut":
            index = int(command[1])
            lenght = int(command[2])
            remove = password[index:(index + lenght)]
            password = password.replace(remove, '', 1)
            print(password)

        elif command[0] == "Substitute":
            substring = command[1]
            substitute = command[2]
            if substring in password:
                password = password.replace(substring, substitute)
                print(password)
            else:
                print("Nothing to replace!")


password_reset()
