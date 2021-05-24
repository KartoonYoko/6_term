import matplotlib.pyplot as plt
import math
import numpy as np
from sympy import *
from sympy.solvers.solveset import linsolve
# variant 17
# x = 1.5 y = 0.43

x = [-1.2, -0.5, 0.4, 1.5, 2.1, 2.9, 3.3, 3.9, 4.3, 5.1]
y = [-2.11, -2.33, -0.14, 0.43, 1.34, 2.65, 6.23, 9.23, 7.65, 4.23]

# S(-1.2) = a10 = y(-1.2) = -2.11
# S(-0.5) = a10 - 0.5 * a11 + x^2 * a12 = y(-0.5) = -2.33
# S(0.4) = a20 + 0.4 * a21 + x^2 * a22 = a30 + 0.4 * a31 + x^2 * a32 = y(0.4) = -0.14
# S(1.5) = a30 + 1.5 * a31 + x^2 * a32 = a40 + 1.5 * a41 + x^2 * a42 = y(1.5) = 0.43
# ...
# S(5.1) = a80 + a81 * 5.1 + a82 * x^2 = y(5.1) = 4.23

# -2.11 - 0.5 * a11 +  0.5^2 * a12 = -2.33
# https://overcoder.net/q/668685/%D0%BA%D0%B0%D0%BA-%D1%80%D0%B5%D1%88%D0%B8%D1%82%D1%8C-%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%83-%D0%BB%D0%B8%D0%BD%D0%B5%D0%B9%D0%BD%D1%8B%D1%85-%D1%83%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B9-%D0%B2-sympy


# Структура, описывающая сплайн на каждом сегменте сетки
class SplineTuple:
    def __init__(self, a, b, c, x, y):
        self.a = a
        self.b = b
        self.c = c
        self.x = x
        self.y = y

    def print_spline(self):
        print('{a} + {x} * {b} + {x}^2 * {c} = {y}'.format(a=self.a, b=self.b, c=self.c, y=self.y, x=self.x))

    def get_spline(self):
        return '{a} + {x} * {b} + {x} ** 2 * {c} - {y}'.format(a=self.a, b=self.b, c=self.c, y=self.y, x=self.x)


def BuildSpline(x, y, n):
    """
        # Построение сплайна
        # x - узлы сетки, должны быть упорядочены по возрастанию, кратные узлы запрещены
        # y - значения функции в узлах сетки
        # n - количество узлов сетки
    """
    # количество сплайнов
    amount = (n - 1)
    # Инициализация массива функций для вычисления сплайнов (их в2 раза больше чем сплайнов)
    splines = [SplineTuple("none", "none", "none", "none", "none") for _ in range(0, amount * 2)]
    # массив для слау (понадобится при вычислении)
    sp_lin = []

    for i in range(amount):
        for j in range(2):
            if j == 1:
                splines[i * 2 + j].x = x[i + 1]
                splines[i * 2 + j].y = y[i + 1]
            else:
                splines[i * 2 + j].x = x[i]
                splines[i * 2 + j].y = y[i]

            splines[i * 2 + j].a = "a" + str(i + 1) + "0"
            splines[i * 2 + j].b = "a" + str(i + 1) + "1"
            splines[i * 2 + j].c = "a" + str(i + 1) + "2"

            sp_lin.append(splines[i * 2 + j].get_spline())

    # добавим доп функции из условий равенства для единственного решения
    if amount % 2 == 0:
        amount_of_equalls = int(amount / 2)
    else:
        amount_of_equalls = int(amount - 1) / 2
    x_iterrator = 1
    for i in range(amount_of_equalls):
        sp_tp1 = SplineTuple("none", "none", "none", "none", "none")
        sp_tp1.a = "a" + str(i + 1) + "0"
        sp_tp1.b = "a" + str(i + 1) + "1"
        sp_tp1.c = "a" + str(i + 1) + "2"
        sp_tp1.x = x[x_iterrator]
        sp_tp2 = SplineTuple("none", "none", "none", "none", "none")
        sp_tp2.a = "a" + str(i + 2) + "0"
        sp_tp2.b = "a" + str(i + 2) + "1"
        sp_tp2.c = "a" + str(i + 2) + "2"
        sp_tp2.x = x[x_iterrator]
        sp_tp1.y = sp_tp2.a + " * " + str(sp_tp2.x) + "+" + sp_tp2.b + " * " + str(sp_tp2.x) + \
                   " + " + sp_tp2.c + " * " + str(sp_tp2.x)
        x_iterrator += 1
        sp_lin.append(sp_tp1.get_spline())

    # добавим доп функции из условий равенства с первой производной для единственного решения
    # if amount % 2 == 0:
    #     amount_of_equalls = int(amount / 2)
    # else:
    #     amount_of_equalls = int(amount - 1) / 2
    # x_iterrator = 1
    # for i in range(amount_of_equalls):
    #     sp_tp1 = SplineTuple("none", "none", "none", "none", "none")
    #     sp_tp1.a = "0"
    #     sp_tp1.b = "a" + str(i + 1) + "1"
    #     sp_tp1.c = "" + "2 * " + "a" + str(i + 1) + "2"
    #     sp_tp1.x = x[x_iterrator]
    #     sp_tp2 = SplineTuple("none", "none", "none", "none", "none")
    #     sp_tp1.a = "0"
    #     sp_tp1.b = "a" + str(i + 2) + "1"
    #     sp_tp1.c = "" + "2 * " + "a" + str(i + 2) + "2"
    #     sp_tp1.x = x[x_iterrator]
    #     sp_tp1.y = sp_tp2.a + " * " + str(sp_tp2.x) + "+" + sp_tp2.b + " * " + str(sp_tp2.x) + \
    #                " + " + sp_tp2.c + " * " + str(sp_tp2.x)
    #     x_iterrator += 1
    #     sp_lin.append(sp_tp1.get_spline())

    # заполним массивы для решения СЛАУ
    sp_symbols = ''
    for i in range(amount):
        sp_symbols += "a" + str(i + 1) + "0, " + "a" + str(i + 1) + "1, " + "a" + str(i + 1) + "2" + ", "

    arr = symbols(sp_symbols)
    for key in splines:
        key.print_spline()

    return linsolve(sp_lin, (arr))


x = [0, 0.25, 0.5, 0.75, 1]
y = [2, 3, 5, 4, 6]
ans = BuildSpline(x, y, len(x))

print()
j = 0
for key in ans:
    for i in key:
        print(i)
