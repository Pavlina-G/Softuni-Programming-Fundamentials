text = input()

digit = ''
letter = ''
symbol = ''

for char in text:
    if char.isalnum():
        if char.isdigit():
            digit += char
        else:
            letter += char
    else:
        symbol += char

print(digit)
print(letter)
print(symbol)