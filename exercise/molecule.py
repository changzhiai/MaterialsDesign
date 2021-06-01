import numpy as np
from atom import Atom

class Molecule(list):     ## We inherit from built-in class list
    # __init__ has been removed.  We could extend it with a type-check
    def get_positions(self):
        "Return the positions of all atoms as an Nx3 array"
        pos = []
        for a in self:
            pos.append(a.position)
        return np.array(pos)
    def get_symbols(self):
        "Return a list of the chemical symbols of all atoms"
        symb = []
        for a in self:
            symb.append(a.symbol)
        return symb
    def __repr__(self):
        "The representation - for brevity include only symbols"
        template = "Atoms(N={}, symbols: {})"
        all_symbols = " ".join(self.get_symbols())
        return template.format(len(self), all_symbols)
    def write_to_file(self, filename):
        f = open(filename, "w")
        print(len(self), file=f)
        print("A molecule", file=f)
        template = "{}  {:.3f} {:.3f} {:.3f}"
        for a in self:
            print(template.format(a.symbol, a.position[0], a.position[1], a.position[2]), file=f)
        f.close()
