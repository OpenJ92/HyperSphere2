import numpy as np
from hyperSphere import hyperSphere
from Multiply import Multiply
from Polynomial import Polynomial

class solvePolynomial:
    def __init__(self, poly, iterations = 200):
        self.poly = poly
        self.vector = self.poly.coefficents
        self.normalization = lambda x: x / np.linalg.norm(x)
        self.normal_vector = self.normalization(self.vector)
        self.mult = Multiply(self.poly.order + 1)
        self.sub_space_hyper_sphere = hyperSphere(self.poly.order)
        self.iterations = iterations
        self.o = self.optimize()

    def __call__(self):
        pass

    def optimize(self):
        for i in range(self.iterations):
            domain_, sub_domain = self.sample_domain_sub_domain(domain_ if i > 0 else None)
            domain_ball = self.domain_ball(sub_domain)
            domain_, range_ = self.make_domain_range(domain_, domain_ball)
            measure__index, domain_ = self.measure_(domain_, range_)
        return domain_%2

    def sample_domain_sub_domain(self, domain = None, samples = 100):
        if isinstance(domain, type(None)):
            domain = 2*np.pi*np.random.random_sample(size=(samples, self.mult.dims-1))
        sub_domain = 2*np.pi*np.random.random_sample(size=(samples, self.mult.dims-2))
        return domain, sub_domain

    def domain_ball(self, sub_domain, radius = .5):
        domain_ball = self.sub_space_hyper_sphere(sub_domain)
        domain_ball = np.apply_along_axis(lambda x: (.5/radius)*np.random.random_sample()*x, 1, domain_ball)
        return domain_ball

    def make_domain_range(self, domain, domain_ball):
        domain_ = np.concatenate([q + domain_ball for q in domain], axis=0)
        range_ = self.mult(domain_)
        return domain_, range_

    def measure_(self, domain_, range_, n = 20):
        range_ = np.apply_along_axis(self.normalization, 1, range_)
        measure__ = ((range_ @ self.normal_vector) - 1)**2
        measure__index = np.argpartition(measure__, n)
        print(measure__[measure__index[:n]])
        return measure__index, domain_[measure__index[:n]]

if __name__ == "__main__":
    pol = Polynomial(np.array([5,1,2,3,10,1]))
    sP = solvePolynomial(pol)
