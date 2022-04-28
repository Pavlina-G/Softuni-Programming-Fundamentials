def calculations(longer_word, smaller_word):
    total = 0
    for i in range(len(longer_word)):
        if i < len(smaller_word):
            total += (ord(longer_word[i]) * ord(smaller_word[i]))
        else:
            total += ord(longer_word[i])

    return total


def character_multiplier(words):
    total_sum = 0
    word1 = words[0]
    word2 = words[1]

    if len(word1) >= len(word2):
        total_sum = calculations(word1, word2)
    else:
        total_sum = calculations(word2, word1)
    print(total_sum)


text = input().split(' ')
character_multiplier(text)
