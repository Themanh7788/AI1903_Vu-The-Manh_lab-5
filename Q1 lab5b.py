#1. Creating a list in PythonCreate a Class with instance attributes
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

vehicle = Vehicle(240, 18)
print(vehicle.max_speed, vehicle.mileage)
#2. Create a Vehicle class without any variables and methods
class Vehicle:
    pass