import matplotlib.pyplot as plt
import math
import numpy as np

# variant 17
# x = 1.5 y = 0.43

x = [-1.2, -0.5, 0.4, 1.5, 2.1, 2.9, 3.3, 3.9, 4.3, 5.1]
y = [-2.11, -2.33, -0.14, 0.43, 1.34, 2.65, 6.23, 9.23, 7.65, 4.23]

print(len(x))
print(len(y))
# S(-1.2) = a10 = y(-1.2) = -2.11
# S(-0.5) = a10 - 0.5 * a11 + x^2 * a12 = y(-0.5) = -2.33
# S(0.4) = a20 + 0.4 * a21 + x^2 * a22 = a30 + 0.4 * a31 + x^2 * a32 = y(0.4) = -0.14
# S(1.5) = a30 + 1.5 * a31 + x^2 * a32 = a40 + 1.5 * a41 + x^2 * a42 = y(1.5) = 0.43
# ...
# S(5.1) = a80 + a81 * 5.1 + a82 * x^2 = y(5.1) = 4.23

# -2.11 - 0.5 * a11 +  0.5^2 * a12 = -2.33
# https://overcoder.net/q/668685/%D0%BA%D0%B0%D0%BA-%D1%80%D0%B5%D1%88%D0%B8%D1%82%D1%8C-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%83-%D0%BB%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D1%8B%D1%85-%D1%83%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B9-%D0%B2-sympy