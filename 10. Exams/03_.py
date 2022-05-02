cards = input().split(", ")
number_lines = int(input())

while number_lines != 0:
    number_lines -= 1
    command = input()
    info = command.split(", ")
    action = info[0]

    if action == "Add":
        card_name = info[1]
        if card_name in cards:
            print("Card is already in the deck")
        else:
            cards.append(card_name)
            print("Card successfully added")

    elif action == "Remove":
        card_name = info[1]
        if card_name in cards:
            cards.remove(card_name)
            print("Card successfully removed")
        else:
            print("Card not found")

    elif action == "Remove At":
        index = int(info[1])
        if index in range(len(cards)):
            cards.pop(index)
            print("Card successfully removed")
        else:
            print("Index out of range")

    elif action == "Insert":
        index = int(info[1])
        card_name = info[2]
        if index in range(len(cards)):
            if card_name not in cards:
                cards.insert(index, card_name)
                print("Card successfully added")
            else:
                print("Card is already added")
        else:
            print("Index out of range")

print(", ".join(cards))
