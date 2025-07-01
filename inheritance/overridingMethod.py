# The overriding method allows a child class to provide specific implementation
# of a method that is provided by one of it's parent classes

class Employee:
    def __init__(self, name, base_pay):
        self.name = name
        self.base_pay = base_pay

    def getPay(self):
        return self.base_pay

class SalesEmployee(Employee):
    def __init__(self, name, base_pay, commision):
        self.name = name 
        self.base_pay = base_pay
        self.commision = commision

    def getPay(self):
        return self.base_pay + self.commision


# lets create a new instance of a sales employee and see her income

# uncomment the next code to see the problem

# john = SalesEmployee("John jakes", 1000, 100)

# print(john.getPay())
# okay so you have noticed that this is only returning the base pay as
# her only pay from the  method in the parent getPay so what about
# her income from the commission

# so here is the fix but a simple one

if __name__ == "__main__":
    jonny = SalesEmployee("John", 15000, 1000)
    print(jonny.getPay())

    jane = Employee("Jane", 10000)

    print(jane.getPay())


# Research on other methods