# Polymorphism Example in Python: Animal, Dog, and Cat Classes
# This program demonstrates polymorphism where different objects (Dog, Cat) 
# provide their own implementation of a common method (sound).

# Parent class (Base class)
class Animal:
    # Method to make a generic sound (to be overridden in child classes)
    def sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Child class Dog that inherits from Animal
class Dog(Animal):
    # Overriding the sound method to return a dog-specific sound
    def sound(self):
        return "Bark"

# Child class Cat that inherits from Animal
class Cat(Animal):
    # Overriding the sound method to return a cat-specific sound
    def sound(self):
        return "Meow"

# Child class Cow that inherits from Animal
class Cow(Animal):
    # Overriding the sound method to return a cow-specific sound
    def sound(self):
        return "Moo"

# Function that demonstrates polymorphism by calling the sound method on any animal
def animal_sound(animal):
    print(animal.sound())

# Creating objects of different classes
dog = Dog()
cat = Cat()
cow = Cow()

# Using polymorphism: the same function works for different types of animals
animal_sound(dog)  # Output: Bark
animal_sound(cat)  # Output: Meow
animal_sound(cow)  # Output: Moo
