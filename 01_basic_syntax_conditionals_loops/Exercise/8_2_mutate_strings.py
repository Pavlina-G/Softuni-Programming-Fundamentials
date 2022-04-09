first_word = input()
second_word = input()

for i in range(len(first_word)):
    if first_word[i] != second_word[i]:
        first_word = first_word[:i] + first_word[i:i + 1].replace(first_word[i], second_word[i]) + first_word[i + 1:]
        print(first_word)

