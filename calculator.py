
from shapes.rectangle import Rectangle
from shapes.square import Square
from shapes.triangle import Triangle
from shapes.circle import Circle
from shapes.hexagon import Hexagon

def main():
    print("=== Area Shape Resolver Calculator ===\n")
    
    shapes = [
        Rectangle(5, 3),
        Square(4),
        Triangle(6, 4),
        Circle(3),
        Hexagon(2)
    ]
    
    for i, shape in enumerate(shapes, 1):
        print(f"{i}. {shape}")
    
if __name__ == "__main__":
    main()
