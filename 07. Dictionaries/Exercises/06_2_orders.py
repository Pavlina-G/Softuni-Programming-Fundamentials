def orders_func(product_details, command):
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])
        # {'Beer': ['1.20', 550], 'Water': ['1.25', '200'], 'IceTea': ['0.50', 220]}

    if product not in product_details:
        product_details[product] = [price, quantity]
    else:
        product_details[product] = [price, (quantity + product_details[product][1])]

    return product_details


def print_func(product_details):
    for item in product_details:
        total_sum = product_details[item][0] * product_details[item][1]
        print(f"{item} -> {total_sum:.2f}")


def orders():
    product_details = {}

    while True:
        command = input()
        if command == "buy":
            print_func(product_details)
            break
        command = command.split(" ")

        product_details = orders_func(product_details, command)


orders()