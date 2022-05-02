text = list(input())
command = input()

while command != "Decode":
    info = command.split("|")
    action = info[0]

    if action == "Move":
        move_number = int(info[1])
        move_text = text[:move_number]
        text = text[move_number:] + move_text

    elif action == "Insert":
        # firstPart = text[:int(info[1])]
        #
        # secondPart = text[int(info[1]):len(text)]
        #
        # text = []
        # for letter in firstPart:
        #     text.append(letter)
        # for letter in info[2]:
        #     text.append(letter)
        # for letter in secondPart:
        #     text.append(letter)

        index = int(info[1])
        value = info[2]
        text = ''.join(text)
        text = text[:index] + value + text[index:]
        text = list(text)

    elif action == "ChangeAll":
        substring = info[1]
        replacement = info[2]
        while substring in text:
            old = text.index(substring)
            text.insert(old + 1, replacement)
            text.pop(old)

    command = input()

print(f"The decrypted message is: {''.join(text)}")