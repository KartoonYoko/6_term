
# 114г задача из первой практике по теории вычеслительных процессов

def func():
    """ """
    sum = 0
    for i in range(1, 129):
        sum += 1 / (2 * i) ** 2
    return sum


print(func())
