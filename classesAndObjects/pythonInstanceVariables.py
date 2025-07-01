 # Unlike class variables Instance variables are bound to a specific instance
 # instance variables are also called instance attributes

from pprint import pprint

class Arch:
    version = "6.12.28"
    kernel = "linux"

pprint(Arch.__dict__)

print(Arch.kernel)
print(Arch.version)

manjaro = Arch() # manjaro is an instance of the arch class and has
                 # its own __dict__

pprint(manjaro.__dict__) # it is empty bcoz it only stores the instance
                         # variables of the object manjaro

print(type(manjaro.__dict__)) # The type is a dictionary
print(type(Arch.__dict__))    # The type is a ? (google it)

# since a dictionary is mutable you can add a new element 
# to the dictionary


# You can accesss the class variables from an instance of a class
# So what hapens is that it checks if the variable are under the
# __dict__ of the class  instance if they are not available it moves
# to the __dict__ of the class of the instance

print(manjaro.kernel)
print(manjaro.version)

