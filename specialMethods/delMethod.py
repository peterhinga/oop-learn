# in python the garbage collector manages memory automatically
# It automaticallly destroys objects that are not referenced
# It is also known as a class finalizer
# In most cases you will rarely use it

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print('__del__ was called')

person = Person("Vanessa", 19)
person = None
