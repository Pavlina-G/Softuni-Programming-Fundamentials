words = input().split(" ")
words = list(map(lambda w: w.lower(), words))
odd_words = []
for word in words:
    if words.count(word) % 2 != 0 and word not in odd_words:
        odd_words.append(word)
print(' '.join(odd_words))

# words_dict = {}
#
# for word in words:
#     if word not in words_dict:
#         words_dict[word] = 1
#     else:
#         words_dict[word] += 1
#
# odd_words = list()
#
# for word in words_dict.keys():
#     if words_dict[word] % 2 != 0:
#         odd_words.append(word)
#
# print(" ".join(odd_words))