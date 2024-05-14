import numpy as np
import math
from scipy.linalg import hadamard

def WHT(x):
    x = np.array(x)
    if len(x.shape) < 2: 
        if len(x) > 3:  
            n = len(x)
            M = math.trunc(math.log(n, 2))
            x = x[0:2 ** M]
            h2 = np.array([[1, 1], [1, -1]])
            for i in range(M - 1):
                if i == 0:
                    H = np.kron(h2, h2)
                else:
                    H = np.kron(H, h2)
            return (np.dot(H, x) / 2. ** M, x, M)

def recursive_WHT(x):
    def recursive_transform(x):
        n = len(x)
        if n == 1:
            return x
        else:
            even = recursive_transform(x[:n//2])
            odd = recursive_transform(x[n//2:])
            return np.concatenate([(even + odd) / 2, (even - odd) / 2])
    x = np.array(x)
    n = len(x)
    # 調整信號的長度為2的冪
    M = int(math.log2(n))
    x = x[:2**M]
    # 遞迴轉換
    result = recursive_transform(x)
    return result, M

def test_recursive_WHT(x_test):
    result_non_recursive = WHT(x_test)[0]
    result_recursive = recursive_WHT(x_test)[0]
    print("recrusive: ", recursive_WHT(x_test))

    if np.array_equal(result_non_recursive, result_recursive):
        print("Solutions are same.")
    else:
        print("Solutions are different.")

test_case1 = [1, 2, 3, 4, 5, 6, 7, 8]
print("testcase1: ", test_case1)
test_recursive_WHT(test_case1)
test_case2 = [1, 4, 3, 2]
print("testcase1: ", test_case2)
test_recursive_WHT(test_case2)