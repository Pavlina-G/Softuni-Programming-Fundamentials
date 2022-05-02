import re

total_income = 0
regex_customer = r"%([A-Z][a-z]+)%"
regex_product = r"<(\w+)>"
regex_count = r"\|(\d+)\|"
regex_price = r"(?<=[\w|\|\W])(?P<price>[0-9.]+[0-9])(?=\$)"

while True:
    line = input()
    current_price = 0

    if line == 'end of shift':
        print(f"Total income: {total_income:.2f}")
        break

    customer = re.findall(regex_customer, line)
    product = re.findall(regex_product, line)
    count = re.findall(regex_count, line)
    price = re.findall(regex_price, line)

    if len(customer) > 0 and len(product)> 0 and len(count) > 0 and len(price) > 0:
        current_price = int(count[0]) * float(price[0])
        total_income += current_price

        print(f'{customer[0]}: {product[0]} - {current_price:.2f}')