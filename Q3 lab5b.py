#1. Define a property that must have the same value for every class instance (object)
class Vehicle:
    color = "White"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    pass
class Car(Vehicle):
    pass
bus = Bus("School Volvo", 180, 12)
print(bus.color, bus.name, "Speed:", bus.max_speed, "Mileage:", bus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)
#2.
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
    def fare(self):
        return self.capacity * 100
class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount
bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", bus.fare())