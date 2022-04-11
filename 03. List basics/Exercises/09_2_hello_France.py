items = input().split("|")
budget = int(input())
profit = 0
new_price_list = []
data_new_prices = []

for item in items:
    condition = False
    current_item = item.split("->")
    item_type = current_item[0]
    price = float(current_item[1])

    if item_type == "Clothes":
        if price <= 50:
            condition = True
    elif item_type == "Shoes":
        if price <= 35:
            condition = True
    elif item_type == "Accessories":
        if price <= 20.50:
            condition = True

    if condition:
        if budget >= price:
            budget -= price
            profit += price * 0.40
            new_price = price + price * 0.40
            new_price_list.append(new_price) #list can be sum
            data_new_prices.append(f"{new_price:.2f}")
            # format:.2f

print(" ".join(data_new_prices))
print(f"Profit: {profit:.2f}")

budget = budget + sum(new_price_list)
if budget >= 150:
    print(f"Hello, France!")
else:
    print(f"Not enough money.")

