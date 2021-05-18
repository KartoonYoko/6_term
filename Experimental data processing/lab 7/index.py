import matplotlib.pyplot as plt
import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
# variant 17
# (5.81, 4.27)
# 7 and 8


def lagranz(x1, x2, y, t1, t2):
    """
    Интерполяционный многочлен Лагранжа для 2 переменых
    :param: list: x1
        список значений аргумента
    :param: list: x2
        список значений второго аргумента
    :param: matrix: y
        значения функции
    :param: float: t1
        значения первого аргумента, для которого вычесляется значение функции
    :param: float: t2
        значения второго аргумента, для которого вычесляется значение функции
    """

    z = 0
    for k in range(len(y)):
        for j in range(len(y[0])):
            p11 = 1
            p12 = 1
            p21 = 1
            p22 = 1
            for i in range(len(x1)):
                if i != j:
                    p11 *= t1-x1[i]
                    p12 *= x1[j]-x1[i]
            for i in range(len(x2)):
                if i != k:
                    p21 *= t2-x2[i]
                    p22 *= x2[k]-x2[i]

            z += y[k][j] * (p11 / p12) * (p21 / p22)
    return z


def measurment_error(const_x1, const_x2, x1, x2, t1, t2):
    """
    поиск погрешности
    """

    def fac(n):
        if n == 0:
            return 1
        return fac(n - 1) * n

    res = 0
    pr = 1
    for i in range(len(x1)):
        pr *= math.fabs(t1 - x1[i])
    res += const_x1 / fac(len(x1) + 1) * pr
    pr = 1
    for i in range(len(x2)):
        pr *= math.fabs(t2 - x2[i])
    res += const_x2 / fac(len(x2) + 1) * pr
    return res


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

tab1 = 5.81
tab2 = 4.27
x_pr = 7
y_pr = 8
print("Значение в точке", tab1, tab2, ":", lagranz(x, y, tab, tab1, tab2))
print("Погрешность:", measurment_error(x_pr, y_pr, x, y, tab1, tab2))

print("Second task ------------------------------------------------------------------------------------------------")
x = np.array([7.31, 7.65, 8.12, 8.67, 8.99, 9.34, 9.89, 5.34, 5.87, 6.88, 7.13, 7.45, 7.89, 8.41, 8.95], dtype=float)
y = np.array([7.34, 5.54, 6.24, 3.76, 4.98, 3.67, 8.35, 7.55, 7.45, 6.54, 4.34, 6.76, 3.43, 2.65, 4.34], dtype=float)
z = np.array([8.98, 8.54, 8.76, 8.45, 4.34, 5.34, 3.45, 9.34, 9.54, 9.34, 3.76, 4.34, 3.34, 5.76, 4.56], dtype=float)


def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n


def combinations(k, n):
    """
    Сочетания
    """
    return fac(n) / (fac(k) * fac(n - k))


def bernstein(x1, x2, z, x, y):
    """
    Бернштейн для 2 размерности
    """
    n = len(x1)
    m = len(x2)
    a = np.min(x1)
    b = np.max(x1)
    c = np.min(x2)
    d = np.max(x2)
    res = 0
    for k in range(n):
        for l in range(m):
            buf = z[l]
            buf *= combinations(k, n) * combinations(l, m)
            buf *= ((x - a) / (b - a)) ** k * (1 - (x - a) / (b - a)) ** (n - k)
            buf *= ((y - c) / (d - c)) ** l * (1 - ((y - c) / (d - c))) ** (m - l)
            res += buf
    return res


znew = []
for i in x:
    for j in y:
        znew.append(bernstein(x, y, z, i, j))
# print(znew)
# plt.plot(x, y, '-')
# plt.grid(True)
# для оценки аппроксимации:
# L / (2 * sqrt(n)) + M / (sqrt(m))
# где M L ограничивают первую частную производную ф-ии z (как найти производную?)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='parametric curve')
plt.show()

