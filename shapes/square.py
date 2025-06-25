from shapes.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side_length):
        self.side_length = side_length
        # Initialize as rectangle with equal sides
        super().__init__(side_length, side_length)
    