# An object of a custom class is associated with a boleeam value
# By default it evaluates to True but we can overide this

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __bool__(self):
        if self.age <= 18:
            return False
        else:
            return True

# We can also use the __len__ method if the custom class does not have the __bool__ method

class Cars:
    def __init__(self, n):
        self.n = n 
    
    def __len__(self):
        print("We are using the method len")
        return self.n

person = Person("Vanessa", 17)
print(bool(person))

cars = Cars(0)
print(bool(cars)) # It will return false

cars.n = 20
print(bool(cars)) # it will return true
