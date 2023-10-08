class MyClass:
    class_variable = 0

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def increment_class_variable(cls):
        cls.class_variable += 1

    @staticmethod
    def say_hello():
        print("Hello from static method!")

    def __str__(self):
        return f"MyClass instance with variable {self.instance_variable}"

MyClass.increment_class_variable()
print("Class variable:", MyClass.class_variable)
MyClass.say_hello()

obj = MyClass(42)
print(obj)
