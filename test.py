import numpy as np
from hyperSphere import hyperSphere
from Multiply import Multiply
from Add import Add

def test_unit(hypS, sample_size):
    sample = np.pi*2*np.random.random_sample((sample_size, hypS.dims-1))
    A = np.apply_along_axis(hypS, 1, sample)
    B = np.apply_along_axis(np.linalg.norm, 1, A)
    return B

def test_angle(hypS, sample_size):
    pass

if __name__ == "__main__":
    hS = hyperSphere(2)
    hS1 = hyperSphere(3)
    n = 1
    A = Multiply(hS, *[hS1 for i in range(n)])
    A_ = Multiply(hS, hS)
    b = Add(hS, *[hS1 for i in range(n)])
