import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from hyperSphere import hyperSphere
from Bezier import bezierCurve
from controlPoints import controlPointsUniformRandomEnclosingPrism

class Loop:
    def __init__(self, domain_in, domain_out,
            control_points=controlPointsUniformRandomEnclosingPrism, 
            samples = 200):
        self.domain_in = domain_in
        self.domain_out = domain_out 
        self.control_points = control_points(self.domain_in, self.domain_out)(2)
        self.bezier = bezierCurve(self.domain_in, self.domain_out, self.control_points).sample(samples)
        self.hyper_sphere = hyperSphere(len(domain_in) + 1)

    def __call__(self):
        return np.apply_along_axis(self.hyper_sphere, 1, self.bezier)

if __name__ == "__main__":
    sample = np.pi*.5*np.ones(2)
    adjust = np.ones_like(sample)*np.pi*2
    l = Loop(sample, sample + adjust)
    
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    e = l()

    ax.scatter3D(*[e[:,i] for i in range(len(l.domain_in)+1)])
    plt.show()

