from shapes.rectangle import Rectangle

class Triangle(Rectangle):
    def __init__(self, base, height):
        super().__init__(base, height)
    
    def get_area(self):
        # Triangle area is half of rectangle area
        return 0.5 * super().get_area()