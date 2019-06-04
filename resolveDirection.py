import numpy as np
from hyperSphere import hyperSphere

class resolveDirection:
    """
        Parameters
        ___________
        vector::np.array : target vector
        hyper_sphere::hyperSphere :  bow and arrow
    """
    def __init__(self, vector, iterations = 100):
        assert np.linalg.norm(vector) > 0
        self.vector = vector
        self.hyper_sphere = hyperSphere(len(self.vector))
        self.sub_space_hyper_sphere = hyperSphere(len(self.vector) - 1)
        self.iterations = iterations
        self.o = self.optimize()

    def __call__(self):
        return self.o

    def optimize(self):
        initial_neighborhood_ball_ = self.initial_neighborhood_ball()
        A = self.make_balls(self.sub_space_hyper_sphere, .1, initial_neighborhood_ball_, 300)
        import pdb;pdb.set_trace()
        return 0

    def initial_neighborhood_ball(self):
        evaluate_sample, sample = self.make_ball(self.hyper_sphere, 1, 300)
        measure_sample = np.apply_along_axis(np.linalg.norm, 1, evaluate_sample - self.vector)
        min_measure = np.argpartition(measure_sample, kth = 10)
        return sample[min_measure[:10]]

    def make_ball(self, hyper_sphere, radius, samples):
        sample = np.random.random_sample(size = (samples * self.hyper_sphere.dims, self.hyper_sphere.dims - 1))
        evaluate_sample = np.apply_along_axis(lambda x: radius*np.random.random_sample()*x,
                                              1,
                                              self.hyper_sphere(sample))
        return evaluate_sample, sample

    def make_balls(self, hyper_sphere, radius, thetas, samples):
        sample = np.random.random_sample(size = (samples, self.hyper_sphere.dims - 1))
        evaluate_sample = np.apply_along_axis(lambda x: radius*np.random.random_sample()*x, 
                                              1, 
                                              self.hyper_sphere(sample))
        import pdb;pdb.set_trace()
        evaluate_sample_ = np.stack([theta + evaluate_sample for theta in thetas], axis = 0)
        return evaluate_sample_


if __name__ == "__main__":
    vector = np.array([1, 0, 0])
    rD = resolveDirection(vector)
