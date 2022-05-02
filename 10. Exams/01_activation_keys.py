raw_key = input()

while True:
    command = input()

    if command == "Generate":
        print(f"Your activation key is: {raw_key}")
        break

    info = command.split('>>>')

    if info[0] == "Contains":
        substring = info[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print(f"Substring not found!")

    elif info[0] == "Flip":
        start_index = int(info[2])
        end_index = int(info[3])
        letters_to_change = info[1]
        swap_text = ''
        if letters_to_change == "Upper":
            swap_text = raw_key[start_index:end_index].upper()
        elif letters_to_change == "Lower":
            swap_text = raw_key[start_index:end_index].lower()
        raw_key = raw_key[:start_index] + swap_text + raw_key[end_index:]
        print(raw_key)

    elif info[0] == "Slice":
        start_index = int(info[1])
        end_index = int(info[2])
        raw_key = raw_key[:start_index] + raw_key[end_index:]
        print(raw_key)
