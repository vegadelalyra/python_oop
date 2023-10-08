# python_oop  

Practicing OOP on Python   

# Object Oriented Programming  

## 4 PILLARS (Abstraction, Inheritance, Encapsulation, Polymorphism)  

![image](https://github.com/vegadelalyra/python_oop/assets/77188420/7d5b8233-7806-4a58-9d99-05a5e97b6c37)  

### Implementation

# Abstraction 
```
from abc import ABC, abstractmethod

class Shape(ABC): # abstract class (python' version of interfaces, interfaces are like contracts)
    @abstractmethod # 'decorator' design pattern
    def area(self):
        pass

class Circle(Shape): # inheritance
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
```

# Inheritance
```
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

```

# Encapsulation

```
class Person:
    def __init__(self, name, age):
        self._name = name  # Single underscore for convention-based encapsulation
        self.__age = age    # Double underscore for name mangling

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if len(new_name) > 0:
            self._name = new_name
        else:
            print("Invalid name.")

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            print("Invalid age.")


# Example usage
person1 = Person("Alice", 25)

# Accessing with single underscore (convention-based encapsulation)
print(person1.get_name())  # Output: Alice
person1.set_name("Alicia")
print(person1.get_name())  # Output: Alicia

# Accessing with double underscore (name mangling)
# This will raise an AttributeError if used outside the class
# print(person1.__age)  # Uncommenting this line would result in an error

# Accessing mangled attribute using the name-mangled form
print(person1._Person__age)  # Output: 25

# Updating age using the setter method
person1.set_age(30)
print(person1.get_age())  # Output: 30
```

# Polymorphism   

```
class Bird:
    def speak(self):
        pass

class Parrot(Bird):
    def speak(self):
        return "Squawk!"

class Sparrow(Bird):
    def speak(self):
        return "Chirp!"

def make_bird_speak(bird):
    return bird.speak()

parrot = Parrot()
sparrow = Sparrow()

print(make_bird_speak(parrot))  # Output: Squawk!
print(make_bird_speak(sparrow))  # Output: Chirp!
```

# SOLID PRINCIPLES    

![image](https://github.com/vegadelalyra/python_oop/assets/77188420/4f7f84a8-eb17-4815-b11b-7396dd40af30)   

# Single Responsibility Principle
```
# file_manager_srp.py

from pathlib import Path
from zipfile import ZipFile

class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

class ZipFileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()

```

# Open Closed Principle  
```
# shapes_ocp.py
from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def calculate_area(self):
        return self.side**2

```

# Liskov Substitution Principle
```
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")

class NewPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")
```

# Dependency Inversion Principle
```
# app_dip.py

from abc import ABC, abstractmethod

class FrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print("Display data:", data)

class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass

class Database(DataSource):
    def get_data(self):
        return "Data from the database"

class API(DataSource):
    def get_data(self):
        return "Data from the API"
```

## BONUS:   

# Design Pattern: Decorator   

One of the most frequently used design patterns in OOP and backend frameworks.   

In this website relies a Python example of the design pattern and a really descriptive explanation of it.   

<pre>
https://refactoring.guru/design-patterns/decorator/python/example
</pre>

![image](https://github.com/vegadelalyra/python_oop/assets/77188420/8e9dd4b7-e30d-4e65-9177-009b3d74df99)

