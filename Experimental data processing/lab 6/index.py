import matplotlib.pyplot as plt
import math
import numpy

# variant 17

# 1.Определить форму связи между факторными и результативными
# признаками, построив корреляционные поля на плоскости для каждой пары факторов.
# Записать уравнение множественной регрессии.
# 2. Произвести отбор факторов, включаемых в модель.
# 3. Определить тесноту связи между факторами, включенными в модель
# множественной линейной корреляции.
# 4. Найти оценки уравнения регрессии по методу наименьших квадратов.
# 5. Проверить адекватность полученного модельного уравнения регрессии тремя
# способами:
# – с помощью коэффициента детерминации R
# 2
# ;
# – по критерию Фишера;
# – с помощью средней ошибки аппроксимации.
# 6. Определить воздействие неучтенных в модели факторов.
# 7. Дать экономическую интерпретацию найденных оценок уравнения регрессии.


y_arr = [
    102, 133.1, 163.3, 192.6, 220.9, 275.1,
    301, 326.1, 350.4, 374, 396.9, 419.9,
    440.6, 461.5, 481.7
]
x1_arr = [1.5, 1.9, 2.4, 2.8, 3.2, 4, 4.4, 4.8, 5.1, 5.5, 5.8, 6.1, 6.4, 6.7, 7]
x2_arr = [2.8, 2.8, 2.7, 2.6, 2.5, 2.4, 2.4, 2.3, 2.2, 2.2, 2.1, 2, 2, 1.9, 1.8]
x3_arr = [3.6, 3.6, 3.5, 3.5, 3.4, 3.4, 3.3, 3.2, 3.2, 3.1, 3.2, 3.1, 3.1, 3, 3.1]
# y_arr = [
#     35, 36, 31, 33, 34, 32, 38, 34, 37, 33
# ]
# x1_arr = [0.92, 0.93, 0.89, 0.9, 0.9, 0.89, 0.92, 0.91, 0.93, 0.89]
# x2_arr = [45, 47, 42, 46, 43, 45, 48, 46, 48, 44]
# x3_arr = [69, 71, 64, 66, 65, 63, 68, 66, 69, 65]
n = len(y_arr)


def forma_print(x: float, str: str = '', signs: str = '2.3'):
    '''
        Выводит форматную строку
        x - число
        str - подпись
        signs - формат для чисел с плавающей точкой (кол-во целых.кол-во полсе точки)
    '''
    string = "{s}: {number:" + signs + "f}"
    print(string.format(s=str, number=x))


def make_graph(is_draw=True):
    '''
        строим корреляционные поля
    '''
    if is_draw:
        # Настройка размеров подложки
        plt.figure(figsize=(15, 12), dpi=90)
        font_graph = 15
        style_graph = '-'
        # Вывод графиков
        plt.subplot(3, 2, 1)
        plt.xlabel('X1', fontsize=font_graph, color='midnightblue')
        plt.ylabel('X2', fontsize=font_graph, color='midnightblue')
        plt.plot(x1_arr, x2_arr, style_graph)   #

        plt.subplot(3, 2, 2)
        plt.xlabel('X2', fontsize=font_graph, color='midnightblue')
        plt.ylabel('X3', fontsize=font_graph, color='midnightblue')
        plt.plot(x2_arr, x3_arr, style_graph)   #

        plt.subplot(3, 2, 3)
        plt.xlabel('X1', fontsize=font_graph, color='midnightblue')
        plt.ylabel('X3', fontsize=font_graph, color='midnightblue')
        plt.plot(x1_arr, x3_arr, style_graph)   #

        plt.subplot(3, 2, 4)
        plt.xlabel('Y',  fontsize=font_graph, color='midnightblue')
        plt.ylabel('X2', fontsize=font_graph, color='midnightblue')
        plt.plot(y_arr, x2_arr, style_graph)

        plt.subplot(3, 2, 5)
        plt.xlabel('Y',  fontsize=font_graph, color='midnightblue')
        plt.ylabel('X1', fontsize=font_graph, color='midnightblue')
        plt.plot(y_arr, x1_arr, style_graph)

        plt.subplot(3, 2, 6)
        plt.xlabel('Y',  fontsize=font_graph, color='midnightblue')
        plt.ylabel('X3', fontsize=font_graph, color='midnightblue')
        plt.plot(y_arr, x3_arr, style_graph)

        plt.show()


make_graph(False)

# найдем коэф парной корреляции
x1_aver = sum(x1_arr) / n
x2_aver = sum(x2_arr) / n
x3_aver = sum(x3_arr) / n
y_aver = sum(y_arr) / n

x1x2_aver = 0
x1x3_aver = 0
x2x3_aver = 0
yx3_aver = 0
yx2_aver = 0
yx1_aver = 0
x1_2_aver = 0
x3_2_aver = 0
for i in range(n):
    x3_2_aver += x3_arr[i] ** 2
    x1_2_aver += x1_arr[i] ** 2
    x1x2_aver += x1_arr[i] * x2_arr[i]
    x1x3_aver += x1_arr[i] * x3_arr[i]
    x2x3_aver += x2_arr[i] * x3_arr[i]
    yx3_aver += y_arr[i] * x3_arr[i]
    yx2_aver += y_arr[i] * x2_arr[i]
    yx1_aver += y_arr[i] * x1_arr[i]
x1x2_aver /= n
x1x3_aver /= n
x2x3_aver /= n
yx3_aver /= n
yx2_aver /= n
yx1_aver /= n
x1_2_aver /= n
x3_2_aver /= n

# S2x1
S2x1 = 0
for i in range(n):
    S2x1 += (x1_arr[i] - x1_aver) ** 2
S2x1 /= n - 1
Sx1 = math.sqrt(S2x1)

# S2x2
S2x2 = 0
for i in range(n):
    S2x2 += (x2_arr[i] - x2_aver) ** 2
S2x2 /= n - 1
Sx2 = math.sqrt(S2x2)
# S2x3
S2x3 = 0
for i in range(n):
    S2x3 += (x3_arr[i] - x3_aver) ** 2
S2x3 /= n - 1
Sx3 = math.sqrt(math.fabs(S2x3))
# S2y
S2y = 0
for i in range(n):
    S2y += (y_arr[i] - y_aver) ** 2
S2y /= n - 1
Sy = math.sqrt(math.fabs(S2y))

# коэфы корреляции
r_x1x2 = (x1x2_aver - x1_aver * x2_aver) / (Sx1 * Sx2)
r_x1x3 = (x1x3_aver - x1_aver * x3_aver) / (Sx1 * Sx3)
r_x2x3 = (x2x3_aver - x2_aver * x3_aver) / (Sx2 * Sx3)
forma_print(r_x1x2, 'Rx1x2', '1.3')
forma_print(r_x1x3, 'Rx1x3', '1.3')
forma_print(r_x2x3, 'Rx2x3', '1.3')

# По найденным коэффициентам парной корреляции видно, что сильно коррелируют
# между собой факторы X2 или X3
print('По найденным коэффициентам парной корреляции видно, что сильно коррелируют между собой факторы X2 или X3.')
print("""Для решения вопроса о том, какой из факторов X2 или 
X3 следует исключить из модели множественной линейной корреляции, вычислим
коэффициенты парной корреляции rYX2 и rYX3.""")
r_x2y = (yx2_aver - y_aver * x2_aver) / (Sy * Sx2)
r_x3y = (yx3_aver - y_aver * x3_aver) / (Sy * Sx3)
forma_print(r_x2y, 'rx2y', '1.3')
forma_print(r_x3y, 'rx3y', '1.3')
print("Так как rYX3 > rYX2, то между признаками X3 и Y связь сильнее, чем между X2 и Y. ")
print("Поэтому из модели множественной линейной корреляции исключаем фактор X2")

r_x1y = (yx1_aver - y_aver * x1_aver) / (Sy * Sx1)
print("Тогда в модель будут включены факторы X1 и X3 и уравнение регрессии запишется в виде")
print("Y12 = a0 + a1 * X1 + a3 * X3")
print("Включение фактора X1 в модель обосновано значимостью коэффициента парной корреляции rYX1:", r_x1y)

# Для выяснения вопроса о силе линейной связи между факторами, включенными в
# модель, вычисляем множественный коэффициент корреляции R по формуле
print("вычисляем множественный коэффициент корреляции ")
R = math.sqrt((r_x1y ** 2 + r_x2y ** 2 - 2 * r_x1x2 * r_x1y * r_x2y) / (1 - r_x1x2 ** 2))
print("Так как в нашем примере объем выборки небольшой (n=" + str(n) + "), то произведем корректировку R")
Rk = math.sqrt(1 - (1 - R ** 2) * (n - 1) / (n - 2))
forma_print(Rk, 'R', '1.3')

# Считаем СЛАУ
# n * a0 + x1_aver * a1 + x3_aver * a2 = y_aver
# x1_aver * a0 + x1_2_aver * a1 + x1x3_aver * a2 = x1y_aver
# x3_aver * a0 + x1x3_aver * a1 + x3_2_aver * a2 = x3y_aver

M1 = numpy.array([[n, x1_aver, x3_aver], [x1_aver, x1_2_aver, x1x3_aver], [x3_aver, x1x3_aver, x3_2_aver]])
v1 = numpy.array([y_aver, yx1_aver, yx3_aver])    # Вектор (правая часть системы)

res = numpy.linalg.solve(M1, v1)

print(""" Тогда 
уравнение регрессии, устанавливающее зависимость производительности труда Y от 
коэффициента нефтеизвлечения X1 и среднего дебита скважин X3 запишется в виде""")
print("Y12 = {a0} + {a1} * X1 + {a3} * X3".format(a0=res[0], a1=res[1], a3=res[2]))


def y12(x1, x3):
    return res[0] + res[1] * x1 + res[2] * x3


print("Проверяем адекватность уравнения регрессии: ")
print("     1) коэф детерминации R")
forma_print(Rk ** 2, "          R %", "1.3")
print("     2) критерий Фишера-Снедекора")
p = 2
Fh = Rk ** 2 * (n - 1 - p) / (p * (1 - Rk ** 2))
forma_print(Fh, "           Fh", "2.3")
print('             F0.05;2;13 = 2.76')
print('             Fh > F => значимо описывает данные')

print("     3) средней ошибки апроксмиации")

eps = 0
for i in range(n):
    circle_buf = y12(x1_arr[i], x3_arr[i])
    eps += math.fabs(y_arr[i] - circle_buf) / y_arr[i]
eps /= p
forma_print(eps * 100, '                eps %', '1.3')
