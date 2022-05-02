import re

text = input()
regex = r"(=|/)+([A-Z][a-zA-Z]{2,})\1"

matches = re.finditer(regex, text)
destinations = []
points = 0

for match in matches:
    destinations.append(match.group(2))
    points += len(match.group(2))

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {points}")
