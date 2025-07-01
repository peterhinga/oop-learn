class Manjaro:
    # class variables are bound to a class and they are shared by
    # all instances of the class

    kernel = "Linux"
    version = "6.12.28"

# To get the class variables we use the dot notation . 

print(Manjaro.kernel)
print(Manjaro.version)

# You can also get the value of a class variable by using the getattr() function
# getattr(class, "variable")

kernel = getattr(Manjaro, "kernel")
print(kernel)

# You can also set the values of the class variable

Manjaro.version = "6.12.25"
print(Manjaro.version)

# You can also use the setattr() function

setattr(Manjaro, "version", "6.12.20")

# since python is a dynamic language you can also add
# class variables at run time

Manjaro.release = "09 May 2025 10:53:27"
print(Manjaro.release)

# You can also set it using the setattr

setattr(Manjaro, "release", "09 May 2025 10:53:27")

print(Manjaro.release)

# If you want to delete the class variables you can use
# the delattr(class, "classVariable")function

delattr(Manjaro, "release")

# you can also use the del keyword

del Manjaro.version

# when you uncommet the below code you will get an error

# print(Manjaro.release)
# print(Manjaro.version)

