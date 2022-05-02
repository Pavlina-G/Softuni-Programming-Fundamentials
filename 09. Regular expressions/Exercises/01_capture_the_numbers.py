import re
text = ''

while True:
    line = input()
    if line:
        text += line + ' '
    else:
        break
regex = r"\d{1,}"

numbers = re.findall(regex, text)

print(' '.join(numbers))


