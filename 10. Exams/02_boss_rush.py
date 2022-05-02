import re

n = int(input())
regex = r"\|(?P<name>[A-Z]{4,})\|:#(?P<title>[a-zA-Z]+\s[a-zA-Z]+)#"

for _ in range(n):
    text = input()
    matches = re.match(regex, text)
    if matches is None:
        print("Access denied!")
    else:
        print(f"{matches.group('name')}, The {matches.group('title')}")
        print(f">> Strength: {len(matches.group('name'))}")
        print(f">> Armor: {len(matches.group('title'))}")


