class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

    def area(self):
        raise NotImplementedError("Area calculation not implemented for this polygon.")

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__([width, height, width, height])
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

if __name__ == "__main__":
    # Test code for the classes
    p = Polygon([3, 4, 5, 6])
    print("Polygon perimeter:", p.perimeter())  # Output: Polygon perimeter: 18
    try:
        print("Polygon area:", p.area())  # Output: NotImplementedError
    except NotImplementedError as e:
        print(e)

    r = Rectangle(3, 4)
    print("Rectangle perimeter:", r.perimeter())  # Output: Rectangle perimeter: 14
    print("Rectangle area:", r.area())  # Output: Rectangle area: 12

    s = Square(5)
    print("Square perimeter:", s.perimeter())  # Output: Square perimeter: 20
    print("Square area:", s.area())  # Output: Square area: 25
