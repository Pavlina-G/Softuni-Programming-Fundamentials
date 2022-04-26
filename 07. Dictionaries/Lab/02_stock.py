products_info = input().split(" ")
searched_products = input().split(" ")
bakery = {}

for i in range(0, len(products_info), 2):
    key = products_info[i]
    value = products_info[i + 1]
    bakery[key] = int(value)

for product in searched_products:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
