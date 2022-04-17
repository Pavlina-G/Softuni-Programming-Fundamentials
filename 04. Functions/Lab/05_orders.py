def total_price(product, quantity):
    if product == "coffee":
        return quantity * 1.50
    elif product == "water":
        return quantity * 1.00
    elif product == "coke":
        return quantity * 1.40
    elif product == "snacks":
        return quantity * 2.00


current_product = input()
current_quantity = int(input())

final_price = total_price(current_product, current_quantity)
print(f"{final_price:.2f}")

