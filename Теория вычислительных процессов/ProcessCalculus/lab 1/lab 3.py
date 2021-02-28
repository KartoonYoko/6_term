
# 63 задача из первой практике по теории вычеслительных процессов

print("""  Определить, верно ли,
что при делении неотрицательного целого числа a на положительное целое число b получается остаток,
равный одному из двух заданных чисел r или s.""")

r = 1
s = 2
x = 0
input_user = True
while input_user:
    x = float(input("> Введите неотрицательное число A: "))
    if (x >= 0):
        input_user = False
    else:
        print("> Введите неотрицательное число!")

y = 0
input_user = True
while input_user:
    y = float(input("> Введите положительное число B: "))
    if (y > 0):
        input_user = False
    else:
        print("> Введите положительное число!")
ost = x % y

print("r: ", r)
print("s: ", s)

if ost == r:
    print("a / b = r")
elif ost == s:
    print("a / b = s")
else:
    print("Остаток от деления ничему не равен")
