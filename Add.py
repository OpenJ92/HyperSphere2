import itertools
import functools
import numpy as np
from itertools import product, zip_longest
from functools import reduce
from Operation import Operation

class Add(Operation):
    def __init__(self, *hyperSpheres):
        super(Add, self).__init__(*hyperSpheres)
        self.str_func = self.make_add()
        exec(self.str_func)
        self.evaluate_function = locals()['hyper_sphere']
        self.dims = sum(self.DomainDims)
    
    def __call__(self, theta):
        return self.evaluate_function(theta)

    def make_add(self):
        shift_ = self.shift()
        container_ = self.container(shift_)
        container_vector_ = self.container_vector(container_)

        function_head = "def hyper_sphere(theta):"
        function_body = f"""{container_vector_}"""[1:-1].replace("'", "").replace("\n", ",").replace(" +", "")
        function_complete = f"""{function_head}
            return {function_body}"""

        return function_complete

    def container_vector(self, container_):
        container_ = [reversed(element) for element in container_]
        container_vector_ = np.empty(shape = max(self.RangeDims), dtype = "O")
        for index, elements in enumerate(zip_longest(*container_, fillvalue = '')):
            expression = reduce(lambda x,y: f"{x}+{y}", elements)
            container_vector_[index] = expression
            print(elements, expression)
        return container_vector_
