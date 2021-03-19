import matplotlib.pyplot as plt
import math


# variant 17

# Ц е л ь р а б о т ы: овладение способами построения моделей линейной корреляции для несгруппированных
# данных, выработка умения и навыков оценки надежности коэффициента корреляции, уравнения регрессии и его коэффициентов.
# С о д е р ж а н и е  а б о т ы: на основании опытных данных требуется:
#  Построить корреляционное поле. По характеру расположения точек в корреляционном поле выбрать
#  общий вид регрессии.
# 2. Вычислить числовые характеристики "x"  ̅, "y"  ̅, 〖" S" 〗_"x" , "S" _"y" , r, 𝜎_"r" .
# 3. Определить значимость коэффициента корреляции r и найти для него доверительный интервал с надежностью ɣ=0,95.
# 4. Написать эмпирические уравнения линий регрессий y на x и xна y.
# 5. Вычислить коэффициент детерминации "R" ^2 и объяснить его смысловое значение.
# 6. Проверить адекватность уравнения регрессии y на x
# 7. Провести оценку величины погрешности уравнения регрессии y
# на x и его коэффициентов.
# 8. Построить уравнение регрессии y на x в первоначальной системе координат.

# Фазовая проницаемость нефти и насыщенность породы нефтью
# Х характеризуется следующими данными:
# X 0.05 0.15 0.25 0.35 0.45 0.55 0.65 0.75 0.85 0.95
# Y 0.35 0.45 0.55 0.65 0.75 0.80 0.85 0.95 1.00 1.25

x_arr = [0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95]
y_arr = [0.35, 0.45, 0.55, 0.65, 0.75, 0.80, 0.85, 0.95, 1.00, 1.25]

# средние значения признаков X Y
x_average = sum(x_arr) / len(x_arr)
y_average = sum(y_arr) / len(y_arr)

# расчет S^2x S^2y выборочные среднеквадратичные отклонения
s2x = 0
s2y = 0
for i in range(len(x_arr)):
    s2x += (x_arr[i] - x_average) ** 2
    s2y += (y_arr[i] - y_average) ** 2
s2x /= len(x_arr) - 1
s2y /= len(y_arr) - 1
sx = math.sqrt(s2x)
sy = math.sqrt(s2y)

# расчет xy- r
xy_average = 0
for i in range(len(x_arr)):
    xy_average += x_arr[i] * y_arr[i]
xy_average /= len(x_arr)
r = round((xy_average - x_average * y_average) / (sx * sy), 3)      # коэф линейной корреляции

# проверяем значимость коэф корреляции
print("проверяем значимость коэф корреляции: ")
tp = round((math.fabs(r) * math.sqrt(len(x_arr) - 2)) / math.sqrt(1 - r ** 2), 2)
print("tp = ", tp , "t = 2.31")

# доверительный интервал для выборочного коэф корреляции r
# с надежностью y = 0.95 поэтому по таблице функции Лапласа
# находим ty = 1.96
ty = 1.96
# средняя квадратичная ошибка
error_aver = round((1 - r ** 2) / (len(x_arr) - 2), 3)
# доверительный интервал тогда
print("доверительный интервал: ")
print(r - ty * error_aver, "<= r^ >=", r + ty * error_aver,)

# уравнения регрессий
print("уравнения регрессий: ")
y_reg = complex(round(y_average - x_average * r * sy / sx, 5), round(r * sy / sx, 5))
x_reg = complex(round(x_average - y_average * r * sx / sy, 5), round(r * sx / sy, 5))
print("y^x = ", y_reg)
print("x^y = ", x_reg)
print("Контроль вычеслений: ")
print(round(y_reg.imag * x_reg.imag, 6))
print(r ** 2)
# Линейные регрессии
yx_arr = []
xy_arr = []
for i in range(len(x_arr)):
    yx_arr.append(round(y_reg.real + y_reg.imag * x_arr[i], 4))
    xy_arr.append(round(x_reg.real + x_reg.imag * y_arr[i], 4))

# коэф детерминации
print("коэф детерминации: ")
print(r ** 2)

# проверим адекватность уравнения линейной регрессии
# y на x по критерию ФИшера-Снедекора
sum1 = 0
sum2 = 0
u_arr = []
for i in range(len(x_arr)):
    u_arr.append((y_arr[i] - yx_arr[i]))
    sum1 += (y_arr[i] - yx_arr[i]) ** 2
    sum2 += (y_arr[i] - y_average) ** 2
u_average = sum1 / len(x_arr)
R2 = 1 - sum1 / sum2
Fh = round(R2 * (len(x_arr) - 2) / (1 - R2), 3)
print("FH = ", Fh, "FT = 5.32")

# проведем оценку величины погрешности уравнения регрессии y_reg
# относительная погрешность
u_average = sum1 / len(x_arr)
sum3 = 0
for i in range(len(x_arr)):
    sum3 += (u_arr[i] - u_average) ** 2
du = round(math.sqrt(sum3 / (len(x_arr) - 2)), 3)
print("du = ", du)
print("Относительная погрешность уравнения y_reg: ", round(du / y_average * 100, 2), "%")

# оценка коэффициентов регрессии
sum3 = 0
for i in range(len(x_arr)):
    sum3 += x_arr[i] ** 2
Syx = sy * math.sqrt(1 - r ** 2)
Sa1 = round(Syx * math.sqrt(len(x_arr) / (len(x_arr) * sum3 - sum(x_arr) ** 2)), 3)
Sa0 = round(Syx * math.sqrt(sum3 / (len(x_arr) * sum3 - sum(x_arr) ** 2)), 3)
print("Sa1 / |a1| = ", Sa1 / math.fabs(y_reg.imag))
print("Sa0 / |a0| = ", Sa0 / math.fabs(y_reg.real))

plt.plot(x_arr, y_arr, 'ro', color="gray", label="Результаты наблюдений")
plt.plot(x_arr, yx_arr, color="blue", label="Линейная регрессия x на y")
plt.plot(xy_arr, y_arr, color="red", label="Линейная регрессия y на x")
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Координатная плоскость')
plt.legend()
plt.grid()      # включение отображение сетки
plt.show()


