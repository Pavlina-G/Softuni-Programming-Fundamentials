def office_chairs(num):
    counter = 0
    free_chairs = 0
    condition = True

    for room in range(1, num + 1):
        counter += 1

        info = input().split(" ")
        chairs = info[0]
        visitors = int(info[1])
        diff = abs(len(chairs) - visitors)

        if len(chairs) < visitors:
            condition = False
            print(f"{diff} more chairs needed in room {counter}")
        elif len(chairs) > visitors:
            free_chairs += diff

    if condition:
        print(f"Game On, {free_chairs} free chairs left")


rooms_number = int(input())
office_chairs(rooms_number)