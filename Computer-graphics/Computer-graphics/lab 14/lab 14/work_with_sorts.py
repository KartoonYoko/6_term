def __greater_than__(a, b):
    return a > b

def __less_than__(a, b):
    return a < b

def sort_indexed_list(data, asc = True):
    """ Function for sorting indexed list """
    compare = __less_than__ if asc else __greater_than__
    for i in range(len(data) - 1):
        m_ind = i
        for j in range(i + 1, len(data)):
            if compare(data[j][1], data[m_ind][1]):
                m_ind = j
        if m_ind != i:
            data[i], data[m_ind] = data[m_ind], data[i]