import math
import numpy as np


def user_input() -> list:
    '''
        Пользовательский ввод для заполнения списка
    '''
    n = int(input("Введите n(размер массива): "))
    arr = []
    for i in range(0, n):
        x = float(input("Введите число: "))
        arr.append(x)
    return arr


def o136(a):
    """
     Формула из 136 о
     """
    sum = 0
    for k in a:
        sum += math.sqrt(10 + k ** 2)
    return sum


def v178(a):
    """
    Определяет количество членов являющихся квадратами четных чисел;
     """
    count = 0
    for k in a:
        buf = math.sqrt(k)
        int_part = buf // 1
        real_part = buf % 1
        if (real_part == 0) and (int_part % 2 == 0):
            count += 1
    return count


def b334(n1, n2):
    """
     Формула из 334 б
     """
    sum_buf = 0
    for i in range(0, n1):
        for j in range(0, n2):
           sum_buf += math.sin(i ** 3 + j ** 4)

    return sum_buf


def a675(arr):
    """ Вставляет столбец а в квадратную
     матрицу arr перед последним столбцом """
    n = len(arr)

    a = np.zeros((n, 1))
    a[0:n, 0:1] = 1

    b = arr[0:n, 0:n-1]
    c = arr[0:n, n-1:n]
    return np.hstack((b, a, c))
