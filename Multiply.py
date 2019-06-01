import itertools
import functools
import numpy as np
from itertools import product
from functools import reduce
from Operation import Operation

class Multiply(Operation):
    def __init__(self, *hyperSpheres):
        super(Multiply, self).__init__(*hyperSpheres)
        self.str_func = self.make_product()
        exec(self.str_func)
        self.evaluate_function = locals()['hyper_sphere']
        self.dims = sum(self.DomainDims)

    def __call__(self, theta):
        return self.evaluate_function(theta)

    def sample(self, sample_size):
        sample_domain = np.random.random_sample(size = (self.dims, sample_size))
        return np.apply_along_axis(self, 0, sample_domain).T

    def make_product(self):
        shift_ = self.shift()
        container_ = self.container(shift_)
        container_hyper_rectangle_ = self.container_hyper_rectangle(container_)
        container_vector_ = self.container_vector(container_hyper_rectangle_)

        function_head = "def hyper_sphere(theta):"
        function_body = f"""{container_vector_}"""[1:-1].replace("'", "").replace("\n", ",")
        function_complete = f"""{function_head}
            return {function_body}"""

        return function_complete

    def container_hyper_rectangle(self, container_):
        hyper_rectangle = np.empty(shape = (self.RangeDims), dtype = "O")
        cartesian_product = product(*self.basis_bounds)

        for index in cartesian_product:
            for sub_index, vector in zip(index, container_):
                if hyper_rectangle[index] == None:
                    hyper_rectangle[index] = f"{vector[sub_index]}"
                else:
                    hyper_rectangle[index] += f"*{vector[sub_index]}"
        
        return hyper_rectangle

    def container_vector(self, container_hyper_rectangle_):
        vector_shape = reduce(lambda x,y: x+y,self.DomainDims) + 1
        container_vector = np.empty(shape = (vector_shape), dtype = "O")
        cartesian_product = product(*self.basis_bounds)

        for index in cartesian_product:
            if container_vector[reduce(lambda x,y: x+y, index)] == None:
                container_vector[reduce(lambda x,y: x+y, index)] = f"{container_hyper_rectangle_[index]}"
            else:
                container_vector[reduce(lambda x,y: x+y, index)] += f"+{container_hyper_rectangle_[index]}"
        return container_vector


