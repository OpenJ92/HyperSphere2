import numpy as np

class hyperSphere:
    def __init__(self, dims):
        self.dims = dims
        self.str_func = self.mhs(dims)
        exec(self.str_func)
        self.hyper_sphere = locals()['hyper_sphere']

    def __call__(self, theta):
        return np.array(self.hyper_sphere(theta))

    def mhs(self, dims):
        function_head = f'def hyper_sphere(theta):'
        function_body = ''
        for j in range(0, dims-1):
            function_body += f"np.cos(theta[{j}])*"
        function_body += '1,'
        for i in range(0, dims-1):
            for j in range(i, dims-1):
                if i == j:
                    function_body += f"np.sin(theta[{j}])"
                else:
                    function_body += f"*np.cos(theta[{j}])"
            function_body += '*1,'
        complete_function = f"""{function_head}
            return {function_body}"""
        return complete_function
