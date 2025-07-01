# inheritance allows a class to reuse the logic of an existing class
# The person class is the parent, base or the super class
# The Employee class is called, drived or subclass of the Person class
# The Employee class derives from, extends or subclasses the Person class

class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello From {self.name}"

class Employee(Person):
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def greet(self):
        return f"Dear {self.name} please change your password"

employee = Employee("Vanessa", "IT")
print(employee.greet())
print(issubclass(Employee, Person))