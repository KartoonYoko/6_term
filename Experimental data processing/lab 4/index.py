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

conditional_value(t, x_arr, y_arr, nx, False)

# Найдем уравнение регрессии
# для этого найдем величины, входящие в это уравнение
max_t = t[0][0]
kef_x = 0
kef_y = 0
for i in range(len(t)):
    for j in range(len(t[0])):
        if max_t < t[i][j]:
            max_t = t[i][j]
            kef_y = j
            kef_x = i
C1 = x_arr[kef_x]   # MoX
C2 = y_arr[kef_y]   # MoY
h1 = x_arr[1] - x_arr[0]    # h1 - шаг X
h2 = y_arr[1] - y_arr[0]    # h2 - шаг Y

u_arr = []
v_arr = []
for i in range(len(x_arr)):
    u_arr.append((x_arr[i] - C1) / h1)
    v_arr.append((y_arr[i] - C2) / h2)

# u средняя
u_average = 0
for i in range(len(x_arr)):
    u_average += nx[i] * x_arr[i]
u_average /= n

# v средняя
v_average = 0
for i in range(len(y_arr)):
    v_average += ny[i] * y_arr[i]
v_average /= n

# u^2 средняя
u_average_2 = 0
for i in range(len(x_arr)):
    u_average_2 += nx[i] * x_arr[i] ** 2
u_average_2 /= n

# v^2 средняя
v_average_2 = 0
for i in range(len(y_arr)):
    v_average_2 += ny[i] * y_arr[i] ** 2
v_average_2 /= n

# Su
Su = math.sqrt(u_average_2 - u_average ** 2)

# Sv
Sv = math.sqrt(v_average_2 - v_average ** 2)

# таблицы для нахождения summ(Nuv * UV)
t2_uv = [
    [],
    [],
    [],
    [],
    [],
    []
]
for i in range(len(t2_uv)):
    for j in range(len(u_arr)):
        t2_uv[i].append(u_arr[i] * v_arr[j])

t2_nuv = [
    [],
    [],
    [],
    [],
    [],
    []
]
for i in range(len(t2_nuv)):
    for j in range(len(u_arr)):
        if t2_uv[i][j] != 0:
            t2_nuv[i].append(t[i][j])
        else:
            t2_nuv[i].append(None)

# Nv
count = 0
for i in range(len(t2_nuv)):
    for j in range(len(u_arr)):
        if t2_nuv[i][j] != None:
            count += t2_nuv[i][j] * t2_uv[i][j]

n_nv = count
# коэф корреляции TODO неверно считает
r = (n_nv - n * u_average * v_average) / (n * Su * Sv)

print(r)
print(n_nv)
print(u_average)
print(v_average)
print(Sv)
print(Su)