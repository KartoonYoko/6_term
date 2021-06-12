def index_min(data)-> int:
    """ Search index minimal element in sequence """
    mi = 0
    m = data[mi]
    for i in range(len(data)):
        if data[i] < m:
            m = data[i]
            mi = i
    return mi


def index_max(data)-> int:
    """ Search index maximal element in sequence """
    mi = 0
    m = data[mi]
    for i in range(len(data)):
        if data[i] > m:
            m = data[i]
            mi = i
    return mi


def list_indices_max(data, count = 1)-> list:
    """ Search some given number indices max elements """
    if count > len(data):
        raise ValueError("Quantity maximums must be less or equal size data!!!")
    indexes = []
    min_val = min(data) - 1
    while count > 0:
        mi = -1
        m = min_val
        for i in range(len(data)):
            if data[i] > m and i not in indexes:
                m = data[i]
                mi = i
        indexes += [mi]
        count -= 1
    return indexes


def list_indices_min(data, count = 1)-> list:
    """ Search some given number indices max elements """
    if count > len(data):
        raise ValueError("Quantity minimums must be less or equal size data!!!")
    indexes = []
    max_val = max(data) + 1
    while count > 0:
        mi = -1
        m = max_val
        for i in range(len(data)):
            if data[i] < m and i not in indexes:
                m = data[i]
                mi = i
        indexes += [mi]
        count -= 1
    return indexes


def list_indices_max_without_min(data, count = 1)-> list:
    """ Search some given number indices max elements """
    if count > len(data):
        raise ValueError("Quantity maximums must be less or equal size data!!!")
    indexes = []
    min_val = min(data) - 1
    while count > 0:
        mi = -1
        m = min_val
        for i in range(len(data)):
            if data[i] > m and i not in indexes:
                m = data[i]
                mi = i
        if m != min_val + 1:
            indexes += [mi]
        count -= 1
    return indexes