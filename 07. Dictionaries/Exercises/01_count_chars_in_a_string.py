# from collections import Counter
#
# word = input()
# result = Counter(word)
#
# for key, value in result.items():
#     if key != ' ':
#         print(f"{key} -> {value}")

text = input()
text_dict = {}

for char in text:
    if char != " ":
        if char not in text_dict:
            text_dict[char] = 1
        else:
            text_dict[char] += 1

for key, value in text_dict.items():
    print(f"{key} -> {value}")
