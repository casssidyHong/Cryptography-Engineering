import numpy as np
from scipy.optimize import curve_fit

def equation(x, a, b):
    return (a * x + b) % 26

# 假設有多組 (x, f(x)) 數據
data = [(4, 8), (10, 26), (27, 7)]  # 舉例

x_values, fx_values = zip(*data)

# 利用整數最小二乘法擬合
params, _ = curve_fit(equation, x_values, fx_values, method='trf')

# 得到最佳擬合的整數 a 和 b 值
a_fit, b_fit = np.round(params).astype(int)

print(f"Best fit coefficients: a = {a_fit}, b = {b_fit}")
