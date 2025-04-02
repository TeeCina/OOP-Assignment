#1.) Creating basic class Nature
class Nature:

#2.) Adding attributes and methods to the Nature class
    # Constructor to initialize the attributes
    # Attributes: name, climate, terrain
    def __init__(self, name, climate, terrain):
        self.name = name
        self.climate = climate
        self.terrain = terrain

# Methods: describe(), sound()
    def describe(self):
        return f"{self.name} has a {self.climate} climate and {self.terrain} terrain."

    def sound(self):
        return "Nature has its own unique sounds."

#3.) Using constructors to initialize the attributes
# Subclass representing a specific aspect of nature: Forest
class Forest(Nature):
    def __init__(self, name, climate, terrain, dominant_tree):
        super().__init__(name, climate, terrain)
        self.dominant_tree = dominant_tree

# Methods: describe(), sound()
    # Overriding the describe method to include dominant tree
    def describe(self):
        return f"{self.name} is a forest with a {self.climate} climate, {self.terrain} terrain, and is dominated by {self.dominant_tree} trees."

    def sound(self):
        return "You can hear birds chirping and leaves rustling in the forest."

# Subclass representing another aspect of nature: Ocean
class Ocean(Nature):
    def __init__(self, name, climate, terrain, salinity_level):
        super().__init__(name, climate, terrain)
        self.salinity_level = salinity_level

# Methods: describe(), sound()
    # Overriding the describe method to include salinity level
    def describe(self):
        return f"{self.name} is an ocean with a {self.climate} climate, {self.terrain} terrain, and a salinity level of {self.salinity_level}."

    def sound(self):
        return "You can hear the waves crashing and the soothing sound of water."

#4.) Adding inheritance layer to explore polymorphism and encapsulation
# Inheritance: Forest and Ocean classes inherit from Nature class
if __name__ == "__main__":

# Creating instances of Ocean class and calling the methods to demonstrate polymorphism and inheritance
    amazon = Forest("Amazon", "tropical", "dense", "mahogany")
# Creating instances of Ocean class and calling it`s` methods to demonstrate polymorphism and inheritance
    pacific = Ocean("Pacific", "varied", "vast", "high")

# Calling the describe and sound methods for both instances
    print(amazon.describe())
    print(amazon.sound())

    print(pacific.describe())
    print(pacific.sound())

##Activity 2: Polymorphism Challenge
# Polymorphism Challenge: Animals and Vehicles with move() method

# Base class: Entity
class Entity:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Subclass: Car
class Car(Entity):
    def move(self):
        return "Driving"

# Subclass: Plane
class Plane(Entity):
    def move(self):
        return "Flying"

# Subclass: Dog
class Dog(Entity):
    def move(self):
        return "Running"

# Subclass: Fish
class Fish(Entity):
    def move(self):
        return "Swimming"

# Demonstrating polymorphism
if __name__ == "__main__":
    entities = [Car(), Plane(), Dog(), Fish()]
    for entity in entities:
        print(entity.move())