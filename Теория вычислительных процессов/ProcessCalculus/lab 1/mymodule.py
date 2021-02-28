import math
import numpy as np


def o136(a):
    """ """
    sum = 0
    for k in a:
        sum += math.sqrt(10 + k ** 2)
    return sum


def v178(a):
    """ """
    count = 0
    for k in a:
        buf = math.sqrt(k)
        int_part = buf // 1
        real_part = buf % 1
        if ((real_part == 0) and (int_part % 2 == 0)):
            count += 1
    return count


def b334():
    """ """
    sum = 0
    for i in range(0, 100):
        for j in range(0, 60):
           sum += math.sin(i ** 3 + j ** 4)

    return sum


def a675(arr):
    """ Вставляет столбец а в квадратную
     матрицу arr перед последним столбцом """
    n = len(arr)

    a = np.zeros((n, 1))
    a[0:n, 0:1] = 1

    b = arr[0:n, 0:n-1]
    c = arr[0:n, n-1:n]
    return np.hstack((b, a, c))
