import re
regex = r"\d+"

while True:
    line = input()

    if not line:
        break

    numbers = re.findall(regex, line)

    if len(numbers) > 0:
        print(' '.join(numbers), end=' ')


