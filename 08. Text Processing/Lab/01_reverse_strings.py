while True:
    word = input()
    reversed_word = ''

    if word == 'end':
        break

    print(f"{word} = {word[::-1]}")
