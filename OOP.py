class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old.")

person1 = Person("John", 30)
person1.introduce()