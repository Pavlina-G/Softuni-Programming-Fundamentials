def force_details_1(force_side, info):
    side = info[0]
    user = info[1]

    condition = [current_side for current_side in force_side if user in force_side[current_side]]
    
    if len(condition) == 0:
        if side not in force_side:
            force_side[side] = [user]
        else:
            force_side[side].append(user)

    return force_side


def force_details_2(force_side, info):
    side = info[1]
    user = info[0]

    for current_side in force_side:
        if user in force_side[current_side]:
            if len(force_side[current_side]) > 1:
                force_side[current_side].pop(user)
                break
            else:
                del force_side[current_side]
                break

    if side not in force_side:
        force_side[side] = [user]
    else:
        force_side[side].append(user)
    print(f"{user} joins the {side} side!")

    return force_side


def force_book():
    force_side = {}

    while True:
        command = input()

        if command == "Lumpawaroo":
            break

        if "|" in command:
            info = command.split(" | ")
            force_side = force_details_1(force_side, info)
        elif "->" in command:
            info = command.split(" -> ")
            force_side = force_details_2(force_side, info)

    for side, users in force_side.items():
        if len(users) > 0:
            print(f"Side: {side}, Members: {len(users)}")
            for user in users:
                print(f"! {user}")


force_book()
