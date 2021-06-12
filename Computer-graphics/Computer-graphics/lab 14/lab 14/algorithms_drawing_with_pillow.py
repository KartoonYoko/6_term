# def draw_line(px_context, x1: int, y1: int, x2: int, y2: int, color = (0, 0, 0)) -> None:
#     """Brezenhem - algorithm drawing line"""
#     lx = abs(x1 - x2)            # define lengths
#     ly = abs(y1 - y2)
#
#     dy = 1 if y1 < y2 else -1    # define direct line
#     dx = 1 if x1 < x2 else -1
#
#     def calculate_brezenhem_cycle(a : int, b : int, da : int, db : int, la : int, lb : int,
#                                   aend : int, aeqlx : bool) -> None:
#         err = 0                                                     # error drawing
#         derr = lb + 1                                               # value incline line
#         while a != aend:
#             px_context[(a, b) if aeqlx else (b, a)] = color         # draw pixel
#             a += da                                                 # go to next point on coordinate a
#             err += derr                                             # increment value error drawing
#             if err >= la + 1:                                       # if error greater (a0 - a1) + 1
#                 err -= la + 1                                       # decrement value error
#                 b += db                                             # go to next point on coordinate b
#
#     if lx > ly:
#         calculate_brezenhem_cycle(x1, y1, dx, dy, lx, ly, x2, True) # angle is belongs [315; 45] and [135; 225]
#     else:
#         calculate_brezenhem_cycle(y1, x1, dy, dx, ly, lx, y2, False) # angle is belongs (45; 135) and (225; 315)



def draw_line(px_context, x1: int, y1: int, x2: int, y2: int, color = (0, 0, 0)):
    """Brezenhem - algorithm drawing line"""
    lx = abs(x1 - x2)            # define lengths
    ly = abs(y1 - y2)

    swap = ly >= lx
    if swap:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        lx, ly = ly, lx

    dy = 1 if y1 < y2 else -1    # define direct line
    dx = 1 if x1 < x2 else -1

    err = 0
    derr = ly + 1
    while x1 != x2:
        px_context[(y1, x1) if swap else (x1, y1)] = color
        x1 += dx
        err += derr
        if err >= lx + 1:
            err -= lx + 1
            y1 += dy


def draw_fill_delta(px_context, p1, p2, p3, fill_color=(0, 0, 0)):
    """algorithm rasterize delta"""
    # ================== sort points ======================
    if p2[1] < p1[1]:
        p1, p2 = p2, p1
    if p3[1] < p1[1]:
        p1, p3 = p3, p1
    if p3[1] < p2[1]:
        p2, p3 = p3, p2
    # ======================================================

    dx13 = dx12 = dx23 = 0

    # ================== calculate dxs =====================
    if p1[1] != p3[1]:
        dx13 = (p3[0] - p1[0]) / (p3[1] - p1[1])
    if p1[1] != p2[1]:
        dx12 = (p2[0] - p1[0]) / (p2[1] - p1[1])
    if p2[1] != p3[1]:
        dx23 = (p3[0] - p2[0]) / (p3[1] - p2[1])
    # ======================================================

    _dx13 = dx13

    x1 = x2 = p1[0]                     # work points in up point

    if dx13 > dx12:
        dx13, dx12 = dx12, dx13

    # ================== case up delta =====================
    for y in range(int(p1[1]), int(p2[1])):
        for x in range(int(x1), int(x2) + 1):
            px_context[x, y] = fill_color           # draw pixel
        x1 += dx13
        x2 += dx12
    # ======================================================

    dx13 = _dx13

    if p1[1] == p2[1]:
        x1 = p1[0]
        x2 = p2[0]

    if dx23 > dx13:
        dx13, dx23 = dx23, dx13

    # ================== case down delta ===================
    for y in range(int(p2[1]), int(p3[1]) + 1):
        for x in range(int(x1), int(x2) + 1):
            px_context[x, y] = fill_color           # draw pixel
        x1 += dx13
        x2 += dx23
    # ======================================================



def point_in_field(x, y, field_size):
    """check point in field"""
    return 0 <= x < field_size[0] and 0 <= y < field_size[1]


def get4neighbours(x, y, field_size):
    """search 4 point's neighbours"""
    p1 = [x, y - 1]
    p2 = [x, y + 1]
    p3 = [x - 1, y]
    p4 = [x + 1, y]
    ans = []

    if point_in_field(*p1, field_size):
        ans += [p1]

    if point_in_field(*p2, field_size):
        ans += [p2]

    if point_in_field(*p3, field_size):
        ans += [p3]

    if point_in_field(*p4, field_size):
        ans += [p4]

    return ans


def fill(px_context, x: int, y: int, size, fill_color = (0, 0, 0)):
    """fill field"""
    queue = []                              # queue points
    curr_point = [x, y]                     # event pixel
    main_color = px_context[x, y]           # field's color
    queue.append(curr_point)
    while len(queue) > 0:
        curr_point = queue.pop()            # get point

        neighbours = get4neighbours(*curr_point, size)                  # get her neighbours
        for neighbour in neighbours:
            if px_context[neighbour[0], neighbour[1]] == main_color:    # check color neighbour-point
                queue.append(neighbour)                                 # add unfilled point

        px_context[curr_point[0], curr_point[1]] = fill_color           # fill this point


def draw_polygon(px_context, size, xc: int, yc: int, r: int, n: int, fill_color=(0, 0, 0)):
    if n < 3:
        raise ValueError("too little angles!!!")
    d = math.pi / 180
    a = 90
    da = (360 / n)
    points = []
    x = xc
    y = yc
    for i in range(n):
        x = xc + r * math.cos(a * d)
        y = yc + r * math.sin(a * d)
        a += da
        points += [[int(x), int(y)]]

    for i in range(n):
        try:
            draw_line(px_context, *points[i], *points[(i + 1) % n])
        except IndexError:
            print("image index out of range!!!")
    fill(px_context, xc + 1, yc + 1, size, fill_color)