import numpy as np
from hyperSphere import hyperSphere

class Solve:
    def __init__(self, function, domain_dimension, pos = None, num_samples = 5000, num_iterations = 500, learning_rate = .01):
        self.function = function
        self.domain_dimension = domain_dimension
        self.sub_domain_dimension = domain_dimension - 1
        self.pos = np.random.random_sample(domain_dimension) if pos == None else pos

        self.hsdd = hyperSphere(domain_dimension)
        self.num_samples = num_samples
        self.num_iterations = num_iterations
        self.learning_rate = learning_rate

    def hyperSphere_sample(self):
        samples = np.pi*2*np.random.random_sample(size = (self.num_samples, self.sub_domain_dimension))
        hyperSphere_sample = np.apply_along_axis(hyperSphere(self.domain_dimension), 1, samples)
        return hyperSphere_sample

    def solve(self):
        while self.num_iterations >= 0:
            hyperSphere_sample = self.learning_rate*self.hyperSphere_sample()
            eval_pos = self.function(self.pos)
            eval_neighborhood = np.apply_along_axis(self.function, 1, self.pos + hyperSphere_sample)
            indexmin = np.argmin(eval_neighborhood) % self.domain_dimension
            print(self.pos, eval_pos, eval_neighborhood[indexmin])
            if eval_pos > eval_neighborhood[indexmin]:
                self.pos += hyperSphere_sample[indexmin]
            self.num_iterations -= 1
        return self.pos

if __name__ == "__main__":
    from functools import reduce
    def f(o):
        i = reduce(lambda x, y: x+y, o)**2
        return i

    s = Solve(f, 3)


