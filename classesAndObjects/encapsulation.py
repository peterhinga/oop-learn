# Encapsulation

# It is the packing of data and functions that work on that data
# within a single object from the outside (information hiding)

class Counter:
    def __init__(self):
        self._current = 0

    def increment(self):
        self._current += 1

    def value(self):
        return self._current

    def reset(self):
        self._current = 0

counter = Counter()

counter.increment()
counter.increment()
counter.increment()

print(counter.value())

# Okay the code works perfectly but there is a problem
# We would like that the default value of counter to not be changed


print(counter.value())

# So how do you ensure that it remains default
# So that is where private attributes comes into play
# Private attributes can only be accessed from class methods
# But not outside

# Python does not have a concept of private attributes
# By convention you can define a private attribute by prefixing
# a single underscore (_)

# Name mangling with double underscores
# If you prefix an attribute with double underscores
# self.__counter pyhton will automatically change name 
# of self.__counter to _class__attribute
# By doing this you cannot access self.__counter 
# directly from outside the class like instance.__attribute
# However you can access it as instance._class__attribute

counter.current = 10 
print(counter.value())

class Counter2:
    def __init__(self):
        self.__current = 0

    def increment(self):
        self.__current += 1

    def value(self):
        return self.__current

    def reset(self):
        self.__current = 0

# The below code will give an error

# counter2 = Counter2()
# print(counter2.__current)

# a work around is

counter2 = Counter2()
print(counter2._Counter2__current)