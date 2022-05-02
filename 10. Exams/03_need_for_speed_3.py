n_cars = int(input())
cars_dict = {}

for n in range(n_cars):
    line = input().split("|")
    car = line[0]
    mileage = int(line[1])
    fuel = int(line[2])

    if car not in cars_dict:
        cars_dict[car] = {'Miles': mileage, 'Fuel': fuel}

command = input()
while command != 'Stop':
    info = command.split(" : ")
    car = info[1]

    if info[0] == "Drive":
        distance = int(info[2])
        fuel = int(info[3])
        if fuel > cars_dict[car]['Fuel']:
            print("Not enough fuel to make that ride")
        else:
            cars_dict[car]['Fuel'] -= fuel
            cars_dict[car]['Miles'] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars_dict[car]['Miles'] >= 100000:
            cars_dict.pop(car)
            print(f"Time to sell the {car}!")

    elif info[0] == "Refuel":
        fuel = int(info[2])
        if cars_dict[car]['Fuel'] + fuel > 75:
            fuel = 75 - cars_dict[car]['Fuel']
            cars_dict[car]['Fuel'] += fuel
        else:
            cars_dict[car]['Fuel'] += fuel
        print(f"{car} refueled with {fuel} liters")

    elif info[0] == "Revert":
        km = int(info[2])
        cars_dict[car]['Miles'] -= km
        if cars_dict[car]['Miles'] < 10000:
            cars_dict[car]['Miles'] = 10000
        else:
            print(f"{car} mileage decreased by {km} kilometers")

    command = input()

for car, value in cars_dict.items():
    print(f"{car} -> Mileage: {value['Miles']} kms, Fuel in the tank: {value['Fuel']} lt.")