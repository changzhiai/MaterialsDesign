import numpy as np
class Atom:
    def __init__(self, symbol, x, y, z):
        self.symbol = symbol
        self.position = np.array([x, y, z])
    def __repr__(self):
        template = "Atom(symbol='{}', position=({:.3f}, {:.3f}, {:.3f}) )"
        return template.format(self.symbol, 
                               self.position[0],
                               self.position[1],
                               self.position[2])
