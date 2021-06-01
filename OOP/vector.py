class Vector:
    """A vector in two dimensions.
    
    Usage:
       Vector(x, y)
    """
    def __init__(self, x, y):
        self.set(x, y)
    def set(self, x, y):
        "Set the coordinates of the vector"
        self.x = x
        self.y = y
    def __add__(self, other):
        "Vector addition"
        return Vector(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return "Vector({:.3f},{:.3f})".format(self.x, self.y)