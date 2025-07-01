# __eq__ method is used to compare two objects by their values

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
# Since Vanessa and Peter are of equal age we want them to be equal
# So we have to implement the __eq__ dunder method

    def __eq__(self, other):
        return self.age == other.age
        
vanessa = Person("Vanessa", 19)
peter = Person("Peter", 19)
shanice = Person("Shanice", 20)
print(shanice.age == 20)
print(peter == vanessa)