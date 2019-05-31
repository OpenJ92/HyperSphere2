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
    sample = np.pi*2*np.random.random_sample((sample_size, hypS.dims))
    A = np.apply_along_axis(hypS, 1, sample)
    a = np.array([1] + [0 for _ in range(max(hypS.RangeDims) - 1)])
    return A @ a.T

if __name__ == "__main__":
    hS = hyperSphere(2)
    hS1 = hyperSphere(3)
    n = 4
    A = Multiply(hS, *[hS1 for i in range(n)])
    b = Add(hS, *[hS1 for i in range(n)])
