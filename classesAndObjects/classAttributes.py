class Circle:
    pi = 3.142 # class attribute 
    # Please ensure it is stored outside the __init__() method
    # Class attributes are useful for storing constants
    # Defining default values
    # Tracking data across all instances


    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        # pi * (radius) sqd
        return self.pi * self.radius**2 # Exponent
    
    def calcCircumference(self):
        return 2 * self.pi * self.radius

circle = Circle(7)
print(circle.calcArea())
print(circle.calcCircumference())