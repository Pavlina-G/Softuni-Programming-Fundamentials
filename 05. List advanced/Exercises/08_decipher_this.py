def decipher(text):

    for word in text:
        num_to_replace = ""
        for i in word:
            if i.isdigit():
                num_to_replace += i
        letter_to_add = chr(int(num_to_replace))
        modify_list = list(word.replace(str(num_to_replace), str(letter_to_add)))
        modify_list[1], modify_list[-1] = modify_list[-1], modify_list[1]
        message_list = "".join(modify_list)
        print(message_list, end=" ")


message = input().split(" ")
decipher(message)