# Example 1: Basic Object
class MyObject:
    def __str__(self):
        if __name__ == '__main__':
            return 'This is an instance of MyObject class'
        else:
            return f'{type(self).__module__}.{type(self).__name__} object at {hex(id(self))}'

# Create an instance of the object
obj = MyObject()    
print(obj)