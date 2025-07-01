class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    @property #simplifys the definition of a property of a class
    def age(self):
        return self.__age

    # You dont really need to declare tis after using the decorator
    # age = property(fget=age)

    # To set the age we can use the following

    @age.setter
    def age(self, age):
        if age <= 0:
            raise ValueError("Age is supposed to be greater than 0")
        
        self.__age = age


v = Person("Vanessa", 19)
print(v._Person__age)