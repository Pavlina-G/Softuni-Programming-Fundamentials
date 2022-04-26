bakery = {}

while True:
    command = input()

    if command == "statistics":
        break

    info = command.split(":")
    product = info[0]
    quantity = int(info[1])

    if product not in bakery:
        bakery[product] = quantity
    else:
        bakery[product] += quantity

print("Products in stock:")
for i in bakery:
    # print('- ' + i + ': ' + str(bakery[i]))
    print(f"- {i}: {bakery[i]}")

print(f"Total Products: {len(bakery)}")
print(f"Total Quantity: {sum(bakery.values())}")


