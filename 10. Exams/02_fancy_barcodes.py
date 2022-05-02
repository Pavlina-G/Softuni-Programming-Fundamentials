import re

n = int(input())
regex = r"(@#+)([A-Z]([a-zA-Z0-9]+){4,}[A-Z])(@#+)"

for i in range(n):
    text = input()
    matches = re.match(regex, text)
    if matches is not None:
        product_group = re.findall(r'\d', matches[0])
        if len(product_group) == 0:
            print(f"Product group: 00")
        else:
            print(f"Product group: {''.join(product_group)}")
    else:
        print("Invalid barcode")

