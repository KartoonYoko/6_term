import matplotlib.pyplot as plt
import math


# variant 17


# 1. Построить корреляционное поле. По характеру расположения точек в корреляционном поле выбрать общий вид регрессии.
# 2. Написать уравнение линии регрессии y на x по методу наименьших квадратов и с использованием коэффициента
#       корреляции r . Сравнить полученные уравнения и сделать вывод о выборе одного из них.
# 3. Оценить тесноту связи между признаками X и Y с помощью выборочного коэффициента корреляции r и его значимость.
# 4. Проверить адекватность модельного уравнения регрессии y на x, записанного через коэффициент корреляции r.
# 5. Проверить надежность уравнения регрессии y на x, записанного через коэффициент корреляции r и его коэффициентов.
# 6. Построить уравнения регрессий в первоначальной системе координат.

x_arr = [20, 22, 24, 26, 28, 30]
y_arr = [100.5, 105.5, 110.5, 115.5, 120.5, 125.5]

nx = [6, 9, 6, 13, 11, 5]
ny = [12, 6, 10, 8, 7, 7]
n = 50

t = [
    [6, 6, 0, 0, 0, 0],
    [0, 3, 2, 1, 0, 0],
    [0, 0, 4, 6, 0, 0],
    [0, 0, 0, 3, 5, 0],
    [0, 0, 0, 3, 4, 0],
    [0, 0, 0, 0, 2, 5]
]


def correlation_field(tab, x_ar, y_ar, is_print=True):
    """
        Строит корреляционное поле
        t, x_arr, y_arr - результаты измерений
    """
    x = []
    y = []
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] != 0:
                x.append(x_ar[j])
                y.append(y_ar[i])

    if is_print:
        plt.plot(x, y, 'oc', label="Корреляционное поле")
        plt.grid()  # включение отображение сетки
        plt.show()


def conditional_value(t, y_arr, x_arr, nx, is_print=True):
    """
    # условное среднее значение признака Y
    """
    y_conditional_value = []

    for i in range(len(t)):
        sum_ = 0
        for j in range(len(t[0])):
            sum_ += t[j][i] * y_arr[j]
        y_conditional_value.append(sum_ / nx[i])

    if is_print:
        plt.plot(x_arr, y_conditional_value, 'oc')
        plt.plot(x_arr, y_conditional_value, '-', color="grey")
        plt.grid()  # включение отображение сетки
        plt.show()


correlation_field(t, x_arr, y_arr, False)

conditional_value(t, x_arr, y_arr, nx)
