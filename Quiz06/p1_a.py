import numpy as np
import math

def WHT_recursive(x):
    x = np.array(x)
    if len(x.shape) < 2: 
        if len(x) > 3:  
            n = len(x)
            M = math.trunc(math.log(n, 2))
            x = x[0:2 ** M]
            return _WHT_recursive(x, M)
        else:
            return x
    else:
        raise ValueError("Input must be a 1D array")

def _WHT_recursive(x, M):
    if M == 0:
        return x
    else:
        h2 = np.array([[1, 1], [1, -1]])
        H = h2
        for i in range(M - 1):
            H = np.kron(H, h2)
        
        if len(x) < 2 ** M:
            x = np.concatenate((x, [0] * (2 ** M - len(x))), axis=0)
        
        return np.dot(H, x) / (2 ** M), M

x_test = [1, 4, 5, 3 ]
result, M = WHT_recursive(x_test)
result = WHT_recursive(x_test)
print("test case:", x_test)
print("Walsh-Hadamard Transform: ", result)
x_test = [2, 7, 4, 2, 3, 1, 6, 2]
result, M = WHT_recursive(x_test)
result = WHT_recursive(x_test)
print("test case:", x_test)
print("Walsh-Hadamard Transform: ", result)