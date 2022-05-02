products = input().split("!")
command = input()

while command != "Go Shopping!":

    info = command.split(" ")
    item = info[1]

    if "Urgent" in command:
        if item not in products:
            products.insert(0, item)
    elif "Unnecessary" in command:
        if item in products:
            products.remove(item)
    elif "Correct" in command:
        if item in products:
            old = products.index(item)
            products.insert(old, info[2])
            products.remove(item)
    elif "Rearrange" in command:
        if item in products:
            products.remove(item)
            products.append(item)
    command = input()

print(", ".join(products))