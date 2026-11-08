# Parent class
class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")


# Child class
class Dog(Animal):

    def bark(self):
        print(self.name, "is barking")


# Creating an object of child class
dog1 = Dog("Tommy")

# Accessing parent class method
dog1.eat()

# Accessing child class method
dog1.bark()
