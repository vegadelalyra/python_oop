class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return print(self.name,'says: woof!')

    def __str__(self):
        return f'Our beloved {self.name}!'
    
dog1 = Dog('Tommy', 3)
dog2 = Dog('Max', 5)

dog1.bark()
print(dog1)

# print(dog1.name)
# print(dog2.age)
