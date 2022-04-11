energy = 100
coins = 100
events = input().split("|")
close_condition = False

for event in events:
    event_info = event.split("-")
    event_data = event_info[0]
    event_number = int(event_info[1])

    if event_data == "rest":
        energy += event_number
        if energy > 100:
            energy = 100
            print(f"You gained 0 energy.")
        else:
            print(f"You gained {event_number} energy.")
        print(f"Current energy: {energy}.")

    elif event_data == "order":
        if energy >= 30:
            energy -= 30
            coins += event_number
            print(f"You earned {event_number} coins.")
        else:
            energy += 50
            print(f"You had to rest!")

    else:
        if coins >= event_number:
            coins -= event_number
            print(f"You bought {event_data}.")
        else:
            close_condition = True
            print(f"Closed! Cannot afford {event_data}.")
            break

if not close_condition:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")


