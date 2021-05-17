import matplotlib.pyplot as plt
import math
import numpy as np

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
# a = []
# a.append([-2.11, 0, 0])
# for i in range(len(x)):
#     pass


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


def BuildSpline(x, y, n):
    """
        # Построение сплайна
        # x - узлы сетки, должны быть упорядочены по возрастанию, кратные узлы запрещены
        # y - значения функции в узлах сетки
        # n - количество узлов сетки
    """
    # количество ур-ий для вычесления сплайнов
    amount = (n - 1) * 2 - 1
    # Инициализация массива функций для вычисления сплайнов
    splines = [SplineTuple("none", "none", "none", "none", "none") for _ in range(0, amount)]

    # т.к. x и y повторяются
    buf = 2
    count = 0
    for i in range(0, amount):
        if (i > 1) and (i < amount - 1):
            if count == 1:
                splines[i].x = x[buf + 1]
                splines[i].y = y[buf + 1]
            else:
                splines[i].x = x[buf]
                splines[i].y = y[buf]
            splines[i].a = "a" + str(buf) + "0"
            splines[i].b = "a" + str(buf) + "1"
            splines[i].c = "a" + str(buf) + "2"
        else:
            # для первых двух случаев и последнего
            # для всего остального - мастеркард
            kef = i
            if i == amount - 1:
                kef = buf
            splines[i].x = x[kef]
            splines[i].y = y[kef]
            kef += 1
            if count == 1:
                kef -= 1
                buf -= 1
            splines[i].a = "a" + str(kef) + "0"
            splines[i].b = "a" + str(kef) + "1"
            splines[i].c = "a" + str(kef) + "2"

        count += 1
        if count == 2:
            count = 0
            buf += 1
        splines[i].print_spline()
    # splines[0].a = str(y[0])
    # splines[0].b = "0"
    # splines[0].c = "0"
    # splines[0].y = str(y[0])
    # TODO посчитать вручную первый сплайн
    pass

    return splines


x = [0, 0.25, 0.5, 0.75, 1]
y = [2, 3, 5, 4, 6]
BuildSpline(x, y, len(x))
