def treasure_finder():
    keys = list(map(int, input().split(' ')))
    original_keys = keys.copy()

    while True:
        text = input()
        text_lenght = len(text)
        new_text = ''

        if text == "find":
            break

        for i in range(text_lenght):
            current_char = ord(text[i])
            changed_char = current_char - keys[i]
            new_text += chr(changed_char)
            keys.append(keys[i])

        keys = original_keys

        start_type = new_text.index("&") + 1
        end_type = new_text[start_type:].find("&") + start_type
        start_place = new_text.index("<") + 1
        end_place = new_text.index(">")

        print(f"Found {new_text[start_type:end_type]} at {new_text[start_place:end_place]}")


treasure_finder()
