# The readonly property can be used to define computed 
# properties

#class Rectangle:
 #   def __init__(self, l, w):
  #      self.l = l
  #      self.w = w

   # @property
    #def area(self):
     #   return self.l * self.w

    #@property
    #def perimeter(self):
     #   add = self.l + self.w
      #  endResult = add * 2
        #return endResult

# r = Rectangle(4, 2)
# print(f"The area is {r.area} and the perimeter is {r.perimeter}")

# caching calculated properties
# using an example of a circle

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = None # it is the cache that stores the calculated area
    
    @property
    def radius(self):
        return self.radius
    
    @radius.setter # If the radius changes in the settler reset the area to None
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius can never be an empty digit:")
        
        if value != self.radius:
            self.radius = value
            self.area = None
    @property
    def area(self):
        if self.area is None:
            self.area = 3.142 * self.radius ** 2
        
        return self.area

c = Circle(7)
print(c.area)