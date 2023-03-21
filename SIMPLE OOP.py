class MyClass:
    # Class attribute
    x = 5
    
    # Class method
    def my_method(self):
        print("Hello, World!")
        
# Creating an object of MyClass
my_object = MyClass()

# Accessing class attribute and method using object
print(my_object.x)          # Output: 5
my_object.my_method()       # Output: Hello, World!

# Using the class as an object
def my_function(obj):
    obj.my_method()

class_instance = MyClass()
my_function(class_instance) 
