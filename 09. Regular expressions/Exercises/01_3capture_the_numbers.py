import re
regex = r"\d+"

while True:
    line = input()

    if not line:
        break

    matches = re.finditer(regex, line, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        print(match[0], end=' ')




