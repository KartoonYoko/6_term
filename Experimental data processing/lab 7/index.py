import matplotlib.pyplot as plt
import math
import numpy as np

# variant 17


def lagranz(x, y, t):
    z = 0
    for j in range(len(y)):
        p1 = 1
        p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1*1
                p2 = p2*1
            else:
                p1 = p1*(t-x[i])
                p2 = p2*(x[j]-x[i])
        z = z+y[j]*p1/p2
    return z


x = np.array([5.45, 5.6, 5.75, 5.9, 6.05, 6.2, 6.35, 6.5, 6.65], dtype=float)
y = np.array([3.15, 3.76, 5.34, 5.43, 3.9, 4.43, 4.65], dtype=float)

tab = [
    [8.87, 9.17, 4.65, 4.19, 7.65, 7.98, 1.12, 2.65, 3.43],
    [5.65, 4.54, 5.76, 7.54, 2.76, 3.40, 9.75, 3.76, 2.19],
    [4.65, 2.14, 3.23, 4.54, 3.33, 6.54, 3.65, 6.43, 4.24],
    [4.65, 2.14, 3.23, 4.54, 3.33, 6.54, 3.65, 6.43, 4.24],
    [3.33, 3.33, 2.43, 6.54, 5.34, 5.34, 4.54, 7.54, 5.43],
    [3.33, 3.33, 2.43, 6.54, 5.34, 5.34, 4.54, 7.54, 5.43],
    [3.54, 5.34, 6.54, 4.54, 5.54, 4.40, 6.76, 4.34, 4.76]
]
print(tab)


def bernstein(n, m):
    '''
        двумерный многочлен Бернштейна
    '''
    for k in range(n):
        for k in range(m):
            pass