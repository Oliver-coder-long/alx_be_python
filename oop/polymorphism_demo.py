class Shape:
  def area(self):
    raise NonimplementedError("Derived classes need to override this method")
class Rectangle(Shape):
  def __init__(self, length, width):
    self.length = length
    self.width = width
  def area(self):
    return length * width
class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius
  def area(self):
    return maath.pi * radius ** 2
