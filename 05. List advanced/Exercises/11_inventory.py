def collect(data, item):

    if item not in data:
        data.append(item)

    return data


def drop(data, item):
    if item in data:
        data.remove(item)

    return data


def combine(data, item):
    item_list = item.split(":")
    old_item = item_list[0]
    new_item = item_list[1]
    if old_item in data:
        index_old = data.index(old_item)
        data.insert(index_old + 1, new_item)

    return data


def renew(data, item):
    if item in data:
        data.remove(item)
        data.append(item)

    return data


def collect_items(items):
    while True:
        command = input()
        if command == "Craft!":
            print(", ".join(items))
            break

        info = command.split(" - ")
        item = info[1]

        if info[0] == "Collect":
            items = collect(items, item)
        elif info[0] == "Drop":
            items = drop(items, item)
        elif info[0] == "Combine Items":
            items = combine(items, item)
        elif info[0] == "Renew":
            items = renew(items, item)


text = input().split(", ")
collect_items(text)
