def print_func(product_details):
    for item in product_details:
        total_sum = float(product_details[item][0]) * int(product_details[item][1])
        print(f"{item} -> {total_sum:.2f}")


def orders():
    product_details = {}

    while True:
        command = input()
        if command == "buy":
            print_func(product_details)
            break
        command = command.split(" ")

        for product, price, quantity in zip(command[0::3], command[1::3], command[2::3]):
            if product not in product_details:
                product_details[product] = [price, quantity]
            else:
                product_details[product] = [price, (int(quantity) + int(product_details[product][1]))]
            # {'Beer': ['1.20', 550], 'Water': ['1.25', '200'], 'IceTea': ['0.50', 220]}

orders()