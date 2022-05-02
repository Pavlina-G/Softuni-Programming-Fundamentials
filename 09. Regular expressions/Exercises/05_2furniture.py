import re


regex = r"^>>([a-zA-Z]+)<<(\d+|\d+\.\d+)!(\d+)$"
total_sum = 0

print("Bought furniture:")

while True:
    command = input()

    if command == "Purchase":
        print(f"Total money spend: {total_sum:.2f}")
        break

    matches = re.match(regex, command)

    if matches is not None:
        print(matches.group(1))
        total_sum += float(matches.group(2)) * int(matches.group(3))

