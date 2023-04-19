import random

gg = random.randint(0, 3)
dfh = random.randint(0, 3)

mass = [[0, 0, 0, 0],
        [0, 7, 3, 0],
        [4, 0, 0, 0],
        [0, -0, 0, 5]]


def mass_kill(ar):
    print('_______')
    for i in ar:
        print(*i)
    print('_______')


def ssussyy(_y5):
    sus = []
    for k in range(4):
        for l in range(4):
            if _y5[k][l] == 0:
                sus.append((k, l))
    return sus


def move_left(mas):
    delta = 0
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    for i in range(4):
        for j in range(3):
            if mas[i][j] == mas[i][j + 1] and mas[i][j] != 0:
                mas[i][j] *= 2
                delta += mas[i][j]
                mas[i].pop(j + 1)
                mas[i].append(0)
    return mas, delta


def move_right(mas):
    delta = 0
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.insert(0, 0)
    for i in range(4):
        for j in range(3, 0, -1):
            if mas[i][j] == mas[i][j - 1] and mas[i][j] != 0:
                mas[i][j] *= 2
                delta += mas[i][j]
                mas[i].pop(j - 1)
                mas[i].insert(0, 0)
    return mas, delta


def transpose(mas):
    new_mas = []
    for i in range(4):
        new_mas.append([])
        for j in range(4):
            new_mas[i].append(mas[j][i])
    return new_mas


def move_up(mas):
    mas = transpose(mas)
    mas, delta = move_left(mas)
    mas = transpose(mas)
    return mas, delta


def move_down(mas):
    mas = transpose(mas)
    mas, delta = move_right(mas)
    mas = transpose(mas)
    return mas, delta


def fed(argument, o1, o2):
    rr = random.random()
    if rr <= 0.75:
        argument[o1][o2] = 2
    else:
        argument[o1][o2] = 4
    return argument


def playable(af):
    for i in af:
        for j in i:
            if j == 0:
                return True
    return False
