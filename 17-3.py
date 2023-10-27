class Shape:

    def __init__(self, colour, square):
        self.colour = colour
        self.square = square

    def set_colour(self, c):
        self.colour = c

    def get_colour(self):
        return self.colour

    def set_square(self, s):
        self.square = s

    def get_square(self):
        return self.square


shape = Shape('Red', 4)
print(shape.colour)
print(shape.square)
