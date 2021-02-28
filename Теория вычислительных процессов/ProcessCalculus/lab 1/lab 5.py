import mymodule

# 136o задача из первой практике по теории вычеслительных процессов

print("""
Даны натуральное число n, действительные числа a1,..., an.
""")

n = int(input("Введите n: "))
arr = []
for i in range(0, n):
    x = float(input("Введите число: "))
    arr.append(x)

print(mymodule.o136(arr))