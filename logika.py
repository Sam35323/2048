import random


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


def move_forward(gh):
    for row in gh:
        while 0 in row:
            row.remove(0)
        while len(row) < 4:
            row.insert(0, 0)
    for row in range(4):
        for col in range(3, 0, -1):
            if gh[row][col] == gh[row][col - 1] and gh[row][col] != 0:
                gh[row][col] *= 2
                gh[row].pop(col - 1)
                gh[row].insert(0, 0)
    return gh


def move_backward(gh):
    for row in gh:
        while 0 in row:
            row.remove(0)
        while len(row) < 4:
            row.append(0)
    for row in range(4):
        for col in range(3):
            if gh[row][col] == gh[row][col + 1] and gh[row][col] != 0:
                gh[row][col] *= 2
                gh[row].pop(col + 1)
                gh[row].append(0)
    return gh

def move_forw1rd():
    pass

def slozhnoe_nazvaniye(gh):
    gk = []
    for i in range(4):
        gk.append([])
        for j in range(4):
            gk[i].append(gh[j][i])
    return gk


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

