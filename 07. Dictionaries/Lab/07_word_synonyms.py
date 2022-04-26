number = int(input())
dict_word = {}

for i in range(number):
    word = input()
    synonym = input()

    if word not in dict_word:
        dict_word[word] = list()

    dict_word[word].append(synonym)

for word in dict_word:
    synonyms = ', '.join(dict_word[word])
    print(f"{word} - {synonyms}")