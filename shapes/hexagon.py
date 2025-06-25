from shapes.shape import Shape 
import math
class Hexagon(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return (3 * math.sqrt(3) / 2) * (self.side_length ** 2)
