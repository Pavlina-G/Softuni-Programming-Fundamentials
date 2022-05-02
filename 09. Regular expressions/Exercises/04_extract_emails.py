import re

mails = input()

regex = r"(^|(?<= ))[a-zA-Z0-9]+[._-]?[a-zA-Z0-9]+@([a-zA-Z]+-?[a-zA-Z]+)(\.[a-zA-Z]+-?[a-zA-Z]+){1,}"
matches = re.finditer(regex, mails, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    print(match[0])