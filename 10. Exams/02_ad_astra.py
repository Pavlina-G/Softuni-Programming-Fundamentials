import re

info = input()

regex = r"(#|\|)+(?P<name>[a-zA-Z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>(\d){1,5})\1"

total_calories = 0

matches = re.finditer(regex, info)
for match in matches:
    calories = match.group('calories')
    total_calories += int(calories)

days = int(total_calories / 2000)
print(f"You have food to last you for: {days} days!")

matches = re.finditer(regex, info)
for match in matches:
    print(f"Item: {match.group('name')}, Best before: {match.group('date')}, Nutrition: {match.group('calories')}")

