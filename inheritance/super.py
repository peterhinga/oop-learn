# the super() is used to delegate to the parent class when overiding methods
# The super method can be used to call the methods of the parent class from a child class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello {self.name} you have passed the interview"

class Employee(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.name = name
        self.age = age
        self.job = job
    
    def greet(self):
        return super().greet() + f" and {self.name} you are our new {self.job}"

person = Person("Jon", 19)
employee = Employee("Jon", 19, "Lawyer")

print(person.greet())
print(employee.greet())