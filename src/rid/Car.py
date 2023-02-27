class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The{self.color} car has {self.mileage} miles"

    def drive(self, number):
        self.mileage += number

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        # self.color = color
        if isinstance(value, str):
            self._color = value
        else:
            raise TypeError("Invalid Type")

    @color.deleter
    def color(self):
        raise AttributeError("Attribute cannot be deleted")


first_car = Car("blue", 20_000)
second_car = Car("red", 30_000)
third_car = Car("yellow", 0)
third_car.drive(100)
print()
benz = Car("Toyota", 2000)
benz2 = Car("black", 2000)
print(benz.color)
print(benz2.color)
benz.color = "Blue"
print(benz.color)
