class Dog: # naming convention for classes is camelcase (e.g., DogType)
    def __init__(self, name, colour):
        self.animal_kind = "canine"         # initialising an attribute
        self.name = name                    # instantiation - creating an instance of an object
        self.colour = colour
        print(self.bark())

    def bark(self):
        return "woof"


jeff = Dog("Jeff", "golden")
bugsy = Dog("Bugsy", "black")

print(jeff)      # This returns a hash which is where the object is stored
print(bugsy)

print(jeff.name)     # This returns the specified attribute
print(bugsy.colour)
print(jeff.animal_kind)
print(type(jeff))
