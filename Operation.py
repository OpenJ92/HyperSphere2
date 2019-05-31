import itertools
from itertools import product

class Operation:
    def __init__(self, *hyperSpheres):
        self.hyperSpheres = hyperSpheres
        self.terms = len(self.hyperSpheres)
        self.RangeDims = [hS.dims for hS in self.hyperSpheres]
        self.DomainDims = [hS.dims-1 for hS in self.hyperSpheres]
        self.IndexDims = [dom-1 for dom in self.DomainDims]
        self.basis_bounds = [range(upper) for upper in self.RangeDims]
        self.cartesian_product = product(*self.basis_bounds)

    def shift(self):
        shift_ = [hS.str_func[44:] for hS in self.hyperSpheres]
        for term in range(1, self.terms):
            largest_index = sum(self.IndexDims[:term]) + term 
            for index in reversed(range(self.DomainDims[term])):
                shift_[term] = shift_[term].replace(f"[{index}]", f"[{index + largest_index}]")
        return shift_

    def container(self, shift_):
        return [element.split(',')[:-1] for element in shift_]


