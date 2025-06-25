#!/usr/bin/env python3
"""
Area Shape Resolver Calculator
Main module that controls everything
"""

from shapes.rectangle import Rectangle
from shapes.square import Square
from shapes.triangle import Triangle
from shapes.circle import Circle
from shapes.hexagon import Hexagon

def main():
    print("=== Area Shape Resolver Calculator ===\n")
    
    # Create different shapes
    shapes = [
        Rectangle(5, 3),
        Square(4),
        Triangle(6, 4),
        Circle(3),
        Hexagon(2)
    ]
    
    # Display all shapes and their areas
    for i, shape in enumerate(shapes, 1):
        print(f"{i}. {shape}")
    
    print(f"\nTotal shapes created: {len(shapes)}")
    print(f"Total area of all shapes: {sum(shape.get_area() for shape in shapes):.2f}")

if __name__ == "__main__":
    main()
