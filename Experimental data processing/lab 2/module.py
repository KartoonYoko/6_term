import matplotlib.pyplot as plt
import math


def variations(arr, interval_variation, discrete_variation, is_print=True):
    """
    Строит дискретный и вариационный ряды
        arr - массив с признаками X
        xmin - минимальный x в выборке
        k - число интервалов вариационног ряда
        h - длина частичных интервалов
        interval_variation - интервальный ряд
        discrete_variation - дискретный ряд
        is_print - false = не рисовать график
    """
    # Для построения интервального вариационного ряда найдем:
    #   - размах варьирования признака X
    Xmax = max(arr)
    Xmin = min(arr)
    R = Xmax - Xmin

    #   - число интервалов вариационног ряда k
    k = len(arr) ** 0.5

    #   - длину h частичных интервалов
    h = R / k
    countall = 0
    for i in range(1, round(k + 1)):
        begin = Xmin + (i - 1) * h
        if i == k:
            end = Xmin + i * h + 0.0001
        else:
            end = Xmin + i * h
        interval_variation[str(begin) + " - " + str(end)] = 0
        count = 0
        for j in range(0, len(arr)):
            if (arr[j] >= begin) and (arr[j] < end):
                count += 1
        interval_variation[str(begin) + " - " + str(end)] = count
        discrete_variation[round(begin + end, 1) / 2] = count
        countall += count

    if is_print:
        plt.title('Вариационный ряд')
        plt.xlabel('Варианты')
        plt.ylabel('Частоты')
        plt.bar(discrete_variation.keys(), discrete_variation.values(), h - 0.1, alpha=0.5)
        plt.plot(discrete_variation.keys(), discrete_variation.values(), color="red")

        plt.show()


def cumulative(arr, discrete_variation, cumulative, is_print=True):
    """
    Построить график накопительных частот — кумуляту.
        discrete_variation - дискретный ряд
        cumulative - кумуляту, где { x : y } x - варианты, y - накопительные частоты
    """
    len_arr = len(arr)
    count = 0
    for key in discrete_variation:
        count += discrete_variation[key] / len_arr
        cumulative[key] = round(count, 2)

    if is_print:
        plt.title('Кумулятивная кривая')
        plt.xlabel('Варианты')
        plt.ylabel('Накопительные частоты')
        plt.grid()
        plt.plot(cumulative.keys(), cumulative.values(), color="green")
        plt.show()


def emperical_func(arr, emp, cum, is_print=True):
    """
        Нахождение эмперической функции emp и
        отрисовка ее графика
    """
    list_len = len(cum)
    cum_keys = list(cum.keys())
    cum_values = list(cum.values())
    emp["0 - " + str(cum_keys[0])] = 0
    for i in range(0, list_len - 1):
        emp[str(cum_keys[i]) + " - " + str(cum_keys[i + 1])] = cum_values[i]
    emp[str(cum_keys[list_len - 1]) + " - infinity"] = 1

    if is_print:
        arr_x = []
        for key in emp:
            begin = key.find(" - ")
            x1 = float(key[:begin])
            x2 = float(key[begin + 3:])
            x = (x1 + x2) / 2
            arr_x.append(x)

        arr_x = arr_x[1:-1]
        arr_y = list(emp.values())[1:-1]

        #   - размах варьирования признака X
        Xmax = max(arr)
        Xmin = min(arr)
        R = Xmax - Xmin

        #   - число интервалов вариационног ряда k
        k = len(arr) ** 0.5

        #   - длину h частичных интервалов
        h = R / k

        plt.title('Эмперическая функция распределения')
        plt.xlabel('Варианты')
        plt.ylabel('Частоты')
        plt.bar(arr_x, arr_y, h - 0.1, alpha=0.5)

        plt.show()


def unbiased_estimates(arr, dis):
    """
        Нахождение числовых характеристик признака Х
        dis -   Дискретный вариационный ряд, где { x : y } x - варианты, y - частоты

        возвращает
            средняя выборочная (средняя x)
            Среднее квадратичное отклонение (S)
            ассиметрию
            эксцесс
    """
    #   - размах варьирования признака X
    Xmax = max(arr)
    Xmin = min(arr)
    R = Xmax - Xmin

    #   - число интервалов вариационног ряда k
    k = len(arr) ** 0.5

    #   - длину h частичных интервалов
    h = R / k

    # Находим MoX
    dis_values = list(dis.values())
    max_ = 0
    max_key = 0     # хранит варианту, встречающуюся с наибольшей частотой (MoX)
    for key in dis:
        if (dis[key] > max_):
            max_key = key
            max_ = dis[key]

    # Находим MeX
    i = 0
    x1 = 0
    x2 = 0
    for key in dis:
        if (i == 4):
            x1 = key
        if (i == 5):
            x2 = key
        i += 1

    x1 = (x1 + x2) / 2  # делит данные из выборки на равные части (MeX)
    # условные варианты, где ui = (xi= MoX) / h
    u = []
    for key in dis:
        u.append((key - max_key) / h)

    # найдем условные начальные моменты
    M1 = 0
    M2 = 0
    M3 = 0
    M4 = 0

    n = len(arr)
    i = 0
    for key in dis:
        M1 += (dis[key] * u[i])
        M2 += (dis[key] * u[i] ** 2)
        M3 += (dis[key] * u[i] ** 3)
        M4 += (dis[key] * u[i] ** 4)
        i += 1

    M1 /= n
    M2 /= n
    M3 /= n
    M4 /= n

    # Находим среднюю выборочную (средняя x) -------------------------------------
    aver_x_disp = M1 * h + max_key

    # Находим выборочную дисперсию
    dispertion = (M2 - M1 ** 2) * h ** 2
    # Среднее квадратичное отклонение (S) ----------------------------------------
    aver_deviation = math.sqrt(dispertion)
    # Коэффициент вариации
    coef_variation = aver_deviation / aver_x_disp

    # находим центральные моменты третьего и четвертого порядков
    m3 = (M3 - 3 * M2 * M1 + 2 * M1 ** 3) * h ** 3
    m4 = (M4 - 4 * M3 * M1 + 6 * M2 * M1 ** 2 - 3 * M1 ** 4) * h ** 4

    # ассиметрия
    As = m3 / aver_deviation ** 3
    # эксцесс
    Ex = m4 / aver_deviation ** 4 - 3

    # 5. Построить доверительные интервалы для истинного значения измеряемой величины и
    # среднего квадратического отклонения
    #       генеральной совокупности.
    n = len(arr)
    t = 0.3289  # y = 0.95 по таблице Лапласа
    buf = aver_deviation / math.sqrt(n) * t
    # Доверительный интервал:
    buf1 = aver_x_disp - buf
    buf2 = aver_x_disp + buf
    return aver_x_disp, aver_deviation, As, Ex
