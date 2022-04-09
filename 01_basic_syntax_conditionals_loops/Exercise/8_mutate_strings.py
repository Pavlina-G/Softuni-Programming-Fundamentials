first_word = input()
second_word = input()

for i in range(len(first_word)): # i 0,1,2,3...
    # print(first_word[i]) - # k i t t y
    if first_word[i] != second_word[i]: # pass to replacement
        replacement = second_word[i] # store unique letters
        word = first_word[0:i] + replacement + first_word[i + 1:]
        first_word = word
        print(first_word)