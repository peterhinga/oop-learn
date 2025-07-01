class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


james = Person("James", 19)

print(james.age)

# age being an instance attribute of the class Person
# you can assign a value to it in this manner

james.age = 20

print(james.age)

# Suppose you want to prevent the value of james age from
# being set to something outrageous like a negative value

james.age = -19

print(james.age)

# So there are different methods each with a drawback

# first one
# Use of if statement

class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def ageChecker(self, age):
        self.age = age
        if age <= 0:
            raise ValueError("Age cannot be less than or equal to zero:")
        else:
            self.age = 1

james1 = Person1("James", 1)
james1.ageChecker(james1.age)
print(james1.age)

# The problem with this method is that youll have to be repetitive

# Method 2
# To avoid being repetitive you'll need to define a pair of methods
# getter and setter
# This methods provide an interface for accessing an instance attribute
# The getter returns the value of an attribute 
# The setter sets the vale for an attribute

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def setAge(self, age):
        pass # Research 

    def getAge(self):
        pass # Research


james2 = Person2("James", 19)

# This method is by using the property class it is efficient 
# Because of backward compatibility of method 2
class Person3:
    def __init__(self, name, age):
        self.name = name
        self.setAge(age)

    def setAge(self, age):
        if age <= 0:
            raise ValueError("Age must be greater than 0")
        self.age = age

    def getAge(self):
        return self.age

    age = property(fget=getAge, fset=setAge)

james3 = Person3("James", 19)
