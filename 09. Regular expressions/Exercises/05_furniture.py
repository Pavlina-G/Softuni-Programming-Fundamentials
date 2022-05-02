import re

command = input()
regex = r">>([a-zA-Z]+)<<(\d+|\d+\.\d+)!(\d+)"
total_sum = 0
furniture = []

while command != "Purchase":
    matches = re.match(regex, command)

    if matches is not None:
        product = matches[1]
        price = float(matches[2])
        quantity = int(matches[3])
        total_sum += price * quantity
        furniture.append(product)

    command = input()

print(f"Bought furniture:")
if total_sum > 0:
    print('\n'.join(furniture))
print(f"Total money spend: {total_sum:.2f}")
