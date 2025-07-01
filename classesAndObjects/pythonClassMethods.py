class Person:
    def __init__(self, fName, lName, age):
        self.fName = fName
        self.lName = lName
        self.age = age

    def get_full_name(self):
        return f"{self.fName} {self.lName}"

    def introduction(self):
        return f"Hello I am {self.fName} {self.lName} I am {self.age} years old"

    @classmethod
    def guest(cls):
        return Person("Vanessa", "Bundi", 19)

# Calling Python Class Methods
# Class.Method
guest = Person.guest()
print(guest.introduction())

# .guest is a factory method because it returns an new instance of the python class