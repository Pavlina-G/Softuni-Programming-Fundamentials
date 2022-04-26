def parking():
    numbers = int(input())
    registered_cars = {}

    for i in range(numbers):
        command = input().split(" ")
        user = command[1]
        if command[0] == 'register':
            car_plate = command[2]
            if user not in registered_cars:
                registered_cars[user] = car_plate
                print(f"{user} registered {car_plate} successfully")
            else:
                print(f"ERROR: already registered with plate number {car_plate}")
        elif command[0] == 'unregister':
            if user not in registered_cars:
                print(f"ERROR: user {user} not found")
            else:
                registered_cars.pop(user)
                print(f"{user} unregistered successfully")

    for user, car_num in registered_cars.items():
        print(f"{user} => {car_num}")


parking()
