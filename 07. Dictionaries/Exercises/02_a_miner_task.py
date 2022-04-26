def miner_task():
    info = {}

    while True:
        resource = input()

        if resource == "stop":
            break
        quantity = int(input())

        if resource not in info:
            info[resource] = quantity
        else:
            info[resource] += quantity

    for key, value in info.items():
        print(f"{key} -> {value}")


miner_task()
