from sympy import *
from sympy.solvers.solveset import linsolve
import matplotlib.pyplot as plt
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
        amount_of_equalls = int(amount)
    else:
        amount_of_equalls = int(amount - 1)
    x_iterrator = 1
    i = 0
    while i < amount_of_equalls - 2:
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
        sp_tp1.y = "(" + sp_tp2.a + " * " + str(sp_tp2.x) + " + " + sp_tp2.b + " * " + str(sp_tp2.x) + \
                    " + " + sp_tp2.c + " * " + str(sp_tp2.x) + ")"
        sp_lin.append(sp_tp1.get_spline())
        x_iterrator += 1
        i += 1

    # заполним массивы для решения СЛАУ
    sp_symbols = ''
    for i in range(amount):
        sp_symbols += "a" + str(i + 1) + "0, " + "a" + str(i + 1) + "1, " + "a" + str(i + 1) + "2" + ", "

    arr = symbols(sp_symbols)
    for key in splines:
        key.print_spline()
    arr_variables = sp_symbols.split(', ')[:-1]
    arr_another = []    # список с свободными членами
    res = linsolve(sp_lin, (arr))
    for arr_buf in res:
        for key in arr_buf:
            for i in arr_variables:
                if i in str(key):
                    if i not in arr_another:
                        arr_another.append(i)
    print(arr_another)

    # добавим доп функции из условий равенства с первой производной для единственного решения
    if amount % 2 == 0:
        amount_of_equalls = int(amount)
    else:
        amount_of_equalls = int(amount - 1)
    x_iterrator = 1
    i = 0
    while i < amount_of_equalls:
        sp_tp1 = SplineTuple("none", "none", "none", "none", "none")
        sp_tp1.a = "0"
        b1 = "a" + str(i + 1) + "1"
        sp_tp1.b = b1
        c1 = "a" + str(i + 1) + "2"
        sp_tp1.c = "" + "2 * " + c1
        sp_tp1.x = x[x_iterrator]
        sp_tp2 = SplineTuple("none", "none", "none", "none", "none")
        sp_tp2.a = "0"
        b2 = "a" + str(i + 2) + "1"
        sp_tp2.b = b2
        c2 = "a" + str(i + 2) + "2"
        sp_tp2.c = "" + "2 * " + c2
        sp_tp2.x = x[x_iterrator]
        sp_tp1.y = "(" + sp_tp2.a + " * " + str(sp_tp2.x) + "+" + sp_tp2.b + \
                    " + " + sp_tp2.c + " * 2 * " + str(sp_tp2.x) + ")"
        if (b1 in arr_another) or (c1 in arr_another) or (b2 in arr_another) or (c2 in arr_another):
            sp_lin.append((b1 + " + " + c1 + " * 2 * %s" + " - " + sp_tp1.y) % x[x_iterrator])
            # sp_lin.append(sp_tp1.get_spline())
            # print((b1 + " + " + c1 + " * 2 * %s" + " - " + sp_tp1.y) % x[x_iterrator])
            # print(sp_tp1.get_spline())
            # print()

        x_iterrator += 1
        i += 1

    return linsolve(sp_lin, (arr))


ans = BuildSpline(x, y, len(x))

print()
j = 0
res = []
count = 1
for key in ans:
    buf = []
    for i in key:
        if count % 3 == 0:
            buf.append(i)
            res.append(buf)
            buf = []
        else:
            buf.append(i)
        count += 1
y_splines = []

for i in range(len(res)):
    buf = res[i][0] + res[i][1] * x[i] + res[i][2] * x[i] ** 2
    y_splines.append(buf)

plt.plot(x[:-1], y_splines, '-')
plt.grid(True)
plt.show()

