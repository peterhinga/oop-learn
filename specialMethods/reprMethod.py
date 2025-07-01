# The method __repr__ defines behaviour when you pass an instance of a class to the repr()
# It returns the string representation of an object
# The __repr__() returns a string that can be executed and yield the same value as the object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f'Person("{self.name}", "{self.age}")'
    
    def __str__(self):
        return f'("{self.name}", "{self.age}")'

person = Person("Vanessa Kerubo", 19)

print(person)
print(repr(person))

# The main difference between __str__ and __repr__ method
# is intended audiences
# __str__ method retuns a string that is human readable 
# While the __repr__ method returns a string representation
# of an object that is machine-readable