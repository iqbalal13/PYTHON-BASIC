class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print(self.name + " says woof woof!!")


class Cat(Animal):
    def make_sound(self):
        print(self.name + " says meow!!")


for i in range(3):
    animal_name = input("Enter the name of the animal: ")
    try:
        int(animal_name)
        print("Invalid animal name. Please enter a string.")
    except ValueError:
        break

if animal_type.lower() == "dog":
    animal = Dog(animal_name)
elif animal_type.lower() == "cat":
    animal = Cat(animal_name)
else:
    print("Invalid animal type")

animal.make_sound()