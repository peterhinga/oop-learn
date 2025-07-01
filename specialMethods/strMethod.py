# The __str__() method is used to make string representation of a class
# Internally python calls the __str__ method when an instance calls the
# str() method
# The print() function converts all non-keyword arguments to strings by
# passing them to the str() before displaying the string values

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name:{self.name}\nAge:{self.age}\n"

person = Person("Vanessa Kerubo", 19)
print(person)