import re

text = input()
regex = r"(\*\*|::)([A-Z]([a-z]){2,})\1"

cool_threshold = 1
digits = re.findall(r'\d', text)
emojis = []

for digit in digits:
    cool_threshold *= int(digit)
print(f"Cool threshold: {cool_threshold}")

count = 0
matches = re.finditer(regex, text)
coolness = 0

for match in matches:
    count += 1
    coolness = sum([ord(x) for x in match.group(2)])
    if coolness >= cool_threshold:
        emojis.append(match[0])
    coolness = 0

print(f"{count} emojis found in the text. The cool ones are:")
for i in emojis:
    print(i)
