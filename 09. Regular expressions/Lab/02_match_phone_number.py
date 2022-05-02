import re

phone_numbers = input()
regex = r"\+359( |-)2\1\d{3}\1\d{4}\b"

#when we have group,   we use finditer
matches = re.finditer(regex, phone_numbers)

output = list()
for match in matches:
    output.append(match.group())

print(', '.join(output))