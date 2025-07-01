class Person:
    pass

person = Person() # Instance of the class
print(person) # Will show you the object person name and memory address
print(id(person)) # memory address in interger format
# to convert the integer address to hexadecimal
print(hex(id(person)))

# to check if an object is an instance of a class
# isinstnce(object, Class)
print(isinstance(person, Person))

# A class is also an object
# Python creates an object after you define the class

print(Person.__name__)

# A class is an obect of the instance type

print(type(Person))