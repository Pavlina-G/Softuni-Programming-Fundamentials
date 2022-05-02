import re

text = input()
regex = r"\b_[a-zA-Z0-9]+\b"

matches = re.findall(regex, text)
output = []

for match in matches:
    output.append(match[1:])

print(','.join(output))

# matches = re.finditer(regex, text, re.MULTILINE)
#
# for matchNum,match in enumerate(matches, start=1):
#     print(match[0][1:])