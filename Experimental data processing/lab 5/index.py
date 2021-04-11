import matplotlib.pyplot as plt
import math
import numpy

# variant 17
#
# Q         5    15  25   35    45     55
# del P     1.25 1.3 5.25 11.25 17.25  21.25

x_arr = [5, 15, 25, 35, 45, 55]
y_arr = [1.25, 1.3, 5.25, 11.25, 17.25, 21.25]

# Найдем функцию регрессии
# для этого посторим СЛАУ

# коэфы СЛАУ
x_sum = 0       # [x]
x_2_sum = 0     # [x^2]
x_3_sum = 0
x_4_sum = 0
y_sum = 0       # [y]
xy_sum = 0      # [xy]
x_2_y_sum = 0   # [x^2 y]

n_len = len(x_arr)

for i in range(len(x_arr)):
    x_sum += x_arr[i]
    x_2_sum += x_arr[i] ** 2
    x_3_sum += x_arr[i] ** 3
    x_4_sum += x_arr[i] ** 4
    y_sum += y_arr[i]
    xy_sum += x_arr[i] * y_arr[i]
    x_2_y_sum += x_arr[i] ** 2 * y_arr[i]

# Матрица (левая часть системы)
M1 = numpy.array([[n_len, x_sum, x_2_sum], [x_sum, x_2_sum, x_3_sum], [x_2_sum, x_3_sum, x_4_sum]])
v1 = numpy.array([y_sum, xy_sum, x_2_y_sum])    # Вектор (правая часть системы)

res = numpy.linalg.solve(M1, v1)


def func_reg(x, a):
    """
    Функция y^_x = a0 + a1 * x^2 + a3 * x^3
    """
    return a[0] + a[1] * x + a[2] * x ** 2


y_reg = []
for key in x_arr:
    y_reg.append(func_reg(key, res))
plt.title('Функция регрессии')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x_arr, y_arr, 'oc', label="Результаты наблюдений")
plt.plot(x_arr, y_reg, color="blue")
plt.show()


def check_linear(func, kef, x, pr=0.05):
    """
        Проверка необходимого условия для линейной регрессии
        pr - маскимальная разница в % (0.1)
    """
    left = func((x[0] + x[len(x) - 1]) / 2, kef)
    right = (func(x[0], kef) + func(x[len(x) - 1], kef)) / 2
    dif = math.fabs(left - right)
    # print(left, right, dif)
    if (left * pr >= dif) and (right * pr >= dif):
        return True
    else:
        return False


def check_power(func, kef, x, pr=0.05):
    """
        Проверка необходимого условия для степенной регрессии
        pr - маскимальная разница в % (0.1)
    """
    left = func(math.sqrt(x[0] * x[len(x) - 1]), kef)
    right = (math.sqrt(func(x[0], kef) * func(x[len(x) - 1], kef)))
    dif = math.fabs(left - right)
    # print(left, right, dif)
    if (left * pr >= dif) and (right * pr >= dif):
        return True
    else:
        return False


def check_exponential(func, kef, x, pr=0.05):
    """
        Проверка необходимого условия для линейной регрессии
        pr - маскимальная разница в % (0.1)
    """
    left = func((x[0] + x[len(x) - 1]) / 2, kef)
    right = (math.sqrt(func(x[0], kef) * func(x[len(x) - 1], kef)))
    dif = math.fabs(left - right)
    # print(left, right, dif)
    if (left * pr >= dif) and (right * pr >= dif):
        return True
    else:
        return False


def check_hyperbolic1(func, kef, x, pr=0.05):
    """
        Проверка необходимого условия для гиперболической регрессии №1
        pr - маскимальная разница в % (0.1)
    """
    left = func((2 * x[0] * x[len(x) - 1]) / (x[0] + x[len(x) - 1]), kef)
    right = (func(x[0], kef) + func(x[len(x) - 1], kef)) / 2
    dif = math.fabs(left - right)
    # print(left, right, dif)
    if (left * pr >= dif) and (right * pr >= dif):
        return True
    else:
        return False


def check_hyperbolic2(func, kef, x, pr=0.05):
    """
        Проверка необходимого условия для гиперболической регрессии №2
        pr - маскимальная разница в % (0.1)
    """
    left = func((x[0] + x[len(x) - 1]) / 2, kef)
    right = (2 * func(x[0], kef) * func(x[len(x) - 1], kef)) / (func(x[0], kef) + func(x[len(x) - 1], kef))
    dif = math.fabs(left - right)
    # print(left, right, dif)
    if (left * pr >= dif) and (right * pr >= dif):
        return True
    else:
        return False


def check_logarithmic(func, kef, x, pr=0.05):
    """
        Проверка необходимого условия для логарифмической регрессии
        pr - маскимальная разница в % (0.1)
    """
    left = func(math.sqrt(x[0] * x[len(x) - 1]), kef)
    right = (func(x[0], kef) + func(x[len(x) - 1], kef)) / 2
    dif = math.fabs(left - right)
    print(left, right, dif)
    if (left * pr >= dif) and (right * pr >= dif):
        return True
    else:
        return False


print(check_linear(func_reg, res, x_arr))
print(check_logarithmic(func_reg, res, x_arr))
print(check_hyperbolic2(func_reg, res, x_arr))
print(check_power(func_reg, res, x_arr))
print(check_exponential(func_reg, res, x_arr))
print(check_hyperbolic1(func_reg, res, x_arr))
