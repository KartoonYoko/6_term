import numpy as np
import matplotlib.pyplot as plt
import seaborn
from random import random

# # создать случайную матрицу numpy array
# arr = np.array(np.random.randint(1, 10, (5, 5)))    # создание матрицы 5x5 из случайных чисел от 1 до 10
# print("Случайная матрица: ")
# print(arr)

# # решить СЛАУ (numpy)
# # 2x + 5y = 1
# # x - 10y = 3
# M1 = np.array([[2., 5.], [1., -10.]])  # Матрица (левая часть системы)
# v1 = np.array([1., 3.])  # Вектор (правая часть системы)

# print("Решение СЛАУ: ")
# print(np.linalg.solve(M1, v1))

# # построить тепловую карту на основе матрицы
# seaborn.heatmap(arr, annot=True, cmap='coolwarm')
# plt.show()


# # построить гистограмму для всех значений в матрице (seaborn)
# l = []
# for i in range(len(arr)):
#     l.extend(arr[i])
# seaborn.displot(l)
# plt.show()

# построить график любой сложной функции.
# подписи к осям, заголовк графика, легенда, координатная сетка

n = 100     # размерность
y = []
x = np.linspace(1, 10, n)
print(x)
# for i in x:     # функция y = 4 + cos(x ** 2)
y = np.cos(x ** 2) + 4

plt.plot(x, y, label="y = cos(x^2) + 4")
#plt.xlabel('ось x')
#plt.ylabel('ось y')
#plt.title('График')
#plt.grid()      # включение отображение сетки
# plt.show()

# построить график этой же функции с добавлением шума (numpy, matplotlib)
noise = np.random.normal(0, 0.5, n)
y_noise = y
y_noise = y + noise

plt.plot(x, y_noise, label="c шумом")
plt.xlabel('ось x')
plt.ylabel('ось y')
plt.title('График с шумом')
plt.grid(True)
plt.legend()
plt.show()
