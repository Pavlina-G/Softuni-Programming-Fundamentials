number_of_orders = int(input())
total_price = 0

for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    price = price_per_capsule * capsules_count * days
    print(f"The price for the coffee is: ${price:.2f}")
    total_price += price

print(f"Total: ${total_price:.2f}")