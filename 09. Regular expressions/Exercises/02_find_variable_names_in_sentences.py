import re

text = input()
regex = r"\b_{1}([a-z]|[A-Z]|[\d])+\b"

matches = re.finditer(regex, text)
output = []

for match in matches:
    output.append(match.group().replace('_',''))

print(','.join(output))

