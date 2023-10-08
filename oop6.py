class Car:
    num_wheels = 4

    def __init__(self, brand):
        self.brand = brand

print("Number of wheels for all cars:", Car.num_wheels)

car1 = Car("Toyota")
car2 = Car("Honda")

print(f"{car1.brand} has {car1.num_wheels} wheels")
print(f"{car2.brand} has {car2.num_wheels} wheels")
