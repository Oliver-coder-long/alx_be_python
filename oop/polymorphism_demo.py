import math
class Shape:
  def area(self):
    raise NonimplementedError("Derived classes need to override this method")
class Rectangle(Shape):
  def __init__(self, length, width):
    self.length = length
    self.width = width
  def area(self):
    return self.length * self.width
class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius
  def area(self):
    circle_area = math.pi * self.radius ** 2
   
