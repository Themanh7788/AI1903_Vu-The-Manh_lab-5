#1. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    pass

bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", bus.name, "Speed:", bus.max_speed, "Mileage:", bus.mileage)
#2Class Inheritance
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
bus = Bus("School Volvo", 180, 12)
print(bus.seating_capacity())