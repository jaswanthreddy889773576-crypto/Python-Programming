# First class
class Dog:

    def sound(self):
        print("Dog says: Woof Woof")


# Second class
class Cat:

    def sound(self):
        print("Cat says: Meow Meow")


# Creating objects
dog = Dog()
cat = Cat()

# Calling the same method
print("Animal Sounds")

dog.sound()
cat.sound()
