#1. Check type of an object
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
class Bus(Vehicle):
    pass
School_bus = Bus("School Volvo", 12, 50)
print(type(School_bus))
#2. Determine if School_bus is also an instance of the Vehicle class
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
class Bus(Vehicle):
    pass
School_bus = Bus("School Volvo", 12, 50)
print(isinstance(School_bus, Vehicle))