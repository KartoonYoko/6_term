import mymodule
import numpy as np

# 675 задача из первой практике по теории вычеслительных процессов

print("""
Даны действительные числа a1,...,an действительная квадратная матрица порядка n (n ≥ 6). 
Получить действительную матрицу размера n x (n+1), 
вставив в исходную матрицу между пятым и шестым столбцами новый столбец с элементами a1,...,an .
""")

n = 6
arr = np.zeros((n, n))
print(mymodule.a675(arr))
