from asee.atom import Atom
import numpy as np
class Molecule:
    def __init__(self, atoms):
        # Check that atoms is a sequence of atoms objects
        for a in atoms:
            assert isinstance(a, Atom)
        # Store the atoms (making sure they are a list,
        # make a copy of the list in any case)
        self.atoms = list(atoms)
    def get_positions(self):
        "Return the positions of all atoms as an Nx3 array"
        pos = []
        for a in self.atoms:
            pos.append(a.position)
        return np.array(pos)
    def get_symbols(self):
        "Return a list of the chemical symbols of all atoms"
        symb = []
        for a in self.atoms:
            symb.append(a.symbol)
        return symb
    def __repr__(self):
        "The representation - for brevity include only symbols"
        template = "Atoms(N={}, symbols: {})"
        all_symbols = " ".join(self.get_symbols())
        return template.format(len(self.atoms), all_symbols)
    def write_to_file(self, filename):
        f = open(filename, "w")
        print(len(self.atoms), file=f)
        print("A molecule", file=f)
        template = "{}  {:.3f} {:.3f} {:.3f}"
        for a in self.atoms:
            print(template.format(a.symbol, a.position[0], a.position[1], a.position[2]), file=f)
        f.close()

    # The length of the object
    def __len__(self):
        return len(self.atoms)
    
    # Indexing
    def __getitem__(self, n):
        return self.atoms[n]
