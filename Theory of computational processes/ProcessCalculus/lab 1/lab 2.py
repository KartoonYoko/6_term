# 42 задача из первой практике по теории вычеслительных процессов

# Даны действительные числа x, y (x не равно y). Меньшее из этих двух чисел заменить их полусуммой,
# а большее - их удвоенным произведением.

def user_input(x, y):
    """ """
    input_user = True
    while input_user:
        x = float(input('> Введите Х: '))
        y = float(input('> Введите Y: '))
        if (x != y):
            input_user = False
        else:
            print("Введите разные значения")
    return x, y


def half_sum(x, y):
    """ """
    return (x + y) / 2


def double_mult(x, y):
    """ """
    return 2 * (x * y)


x = 0
y = 0
x, y = user_input(x, y)

if (x > y):
    first = x
    second = y
    x = double_mult(first, second)
    y = half_sum(first, second)
else:
    first = x
    second = y
    y = double_mult(first, second)
    x = half_sum(first, second)

print("x: ", x)
print("y: ", y)
