
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create two instances of the Person class
p1 = Person("Vanessa", 19)
p2 = Person("Lucy", 19)

# show the hashes of the instances
# The hash function accepts an object
# and returns the hash in an integer format
print(hash(p1))
print(hash(p2))

# Research more on it