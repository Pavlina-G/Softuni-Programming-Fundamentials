import string

def calculations(word):
    sum = 0
    number = int(word[1:(len(word)-1)])

    if word[0].isupper():
        sum += number / (string.ascii_lowercase.index(word[0].lower()) + 1)
    else:
        sum += number * (string.ascii_lowercase.index(word[0].lower()) + 1)
    if word[-1].isupper():
        sum -= (string.ascii_lowercase.index(word[-1].lower()) + 1)
    else:
        sum += (string.ascii_lowercase.index(word[-1].lower()) + 1)

    return sum


def letter_change_number(data):
    total_sum = 0
    for word in data:
        sum = calculations(word)
        total_sum += sum

    print(f'{total_sum:.2f}')


text = input().split()
letter_change_number(text)
