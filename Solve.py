import numpy as np

class Solve():
    def __init__(self, vector, Obj = "hyperSphere"):
        self.unit_vector = np.linalg.norm(vector) * vector
