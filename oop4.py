from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, fav_toy):
        self.name = name
        self.fav_toy = fav_toy

    def make_sound(self):
        print('growls')

class Dog(Animal):
    def __init__(self, name, age):
        self.name = name + ' Bigotes'
        self.age = age

    def make_sound(self):
        return print(self.name,"says Woof!")

class Cat(Animal):
    def make_sound(self):
        return print("Meow!")


class Robot(Animal):
    def talk():
        return print('Hello, human.')

wahia = Robot('waji', 'stars')
wahia.make_sound()

# class Robo_Dog(Robots)

dog = Dog("Firulais", 1)
cat = Cat("Misifú", 'Mice')

dog.make_sound() # Woof!
cat.make_sound() # Meow!
