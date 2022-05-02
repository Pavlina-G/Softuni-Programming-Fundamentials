command = input()

total_price = 0
vat = 0
while True:
    if command == "special":
        final_price = (total_price + vat) * 0.90
        break
    if command == "regular":
        final_price = total_price + vat
        break

    price = float(command)

    if price > 0:
        total_price += price
        vat += price * 0.20
    else:
        print("Invalid price!")

    command = input()

if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {vat:.2f}$")
    print("-----------")
    print(f"Total price: {final_price:.2f}$")
