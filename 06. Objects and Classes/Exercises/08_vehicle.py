class Vehicle:

    def __init__(self, type_car, model_car, price_car):
        self.type = type_car
        self.model = model_car
        self.price = price_car
        self.owner = None

    def buy(self, money: int, owner: str):
        if money >= self.price and self.owner is None:
            change = money - self.price
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {change:.2f}"

        elif money < self.price:
            return "Sorry, not enough money"

        else:
            return "Car already sold"

    def sell(self):
        if self.owner is None:
            return "Vehicle has no owner"
        else:
            self.owner = None

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
