class Dog:

    color = "black"
    # lass attributes must come before constructor

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age


    def about(self):
        return f" I am {self.name} of breed {self.breed}"

    def make_sound(self):
        return f"{self.name} says Woof Woof"

tommy = Dog("tommy", "caucasian", 3)
flip = Dog("flip", "german shepard", 5)

print(type(tommy) == type(flip))
print(tommy.color)