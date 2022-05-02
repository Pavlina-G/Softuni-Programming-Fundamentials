import re

text = input()
regex = r"(@|#)(?P<first_word>([a-zA-Z]+){3,})\1\1(?P<second_word>([a-zA-Z]+){3,})\1"
valid_pairs = []
count = 0

word_pairs = re.finditer(regex, text)
mirror_words = []

for match in word_pairs:
    valid_pairs.append(match.group('first_word').strip() + " " + match.group('second_word').strip())
    reversed_word = ''.join(reversed(match.group('first_word')))
    if reversed_word == match.group('second_word'):
        mirror_words.append(match.group('first_word') + " <=> " + match.group('second_word'))

if len(valid_pairs) == 0:
    print("No word pairs found!")
else:
    print(f"{len(valid_pairs)} word pairs found!")

if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(sep=', ', *mirror_words)


