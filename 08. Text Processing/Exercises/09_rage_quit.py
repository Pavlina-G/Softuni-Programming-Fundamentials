def counter_unique(output):
    count = set(output)
    return len(count)


def rage(text):
    output = ''
    new_text = ''

    for i in range(len(text)):
        if text[i].isnumeric():
            if i < (len(text)-1):
                if text[i + 1].isnumeric():
                    output += (new_text * int(str(text[i]) + str(text[i+1])))
                    i += 1
                else:
                    output += new_text * int(text[i])
            else:
                output += (new_text * int(text[i]))
            new_text = ''
        else:
            new_text += text[i]

    count = counter_unique(output)
    print(f"Unique symbols used: {count}")
    print(output)


data = input().upper()
rage(data)
