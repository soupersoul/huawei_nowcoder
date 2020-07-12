'''
metrics = []
metrics.append(list(map(int, '0 9 2 4 8 1 7 6 3'.split())))
metrics.append(list(map(int, '4 1 3 7 6 2 9 8 5'.split())))
metrics.append(list(map(int, '8 6 7 3 5 9 4 1 2'.split())))
metrics.append(list(map(int, '6 2 4 1 9 5 3 7 8'.split())))
metrics.append(list(map(int, '7 5 9 8 4 3 1 2 6'.split())))
metrics.append(list(map(int, '1 3 8 6 2 7 5 9 4'.split())))
metrics.append(list(map(int, '2 7 1 5 3 8 6 4 9'.split())))
metrics.append(list(map(int, '3 8 6 9 1 4 2 5 7'.split())))
metrics.append(list(map(int, '0 4 5 2 7 6 8 3 1'.split())))
'''
all_sets = {1, 2, 3, 4, 5, 6, 7, 8, 9}

def find_options(x, y):
    set_row = set(metrics[x])
    set_col = set([r[y] for r in metrics])
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    set_sub = set()
    for yi in range(y0, y0+3):
        for xj in range(x0, x0+3):
            set_sub.add(metrics[xj][yi])
    return all_sets.difference(set_row).difference(set_col).difference(set_sub)

def check(x, y):
    row = set(metrics[x])
    if len(row) < 9:
        return False
    col = set(map(lambda r: r[y], metrics))
    if len(col) < 9:
        return False

def can_fix(x, y):
    while True:
        if metrics[x][y] == 0:
            options = find_options(x, y)
            if not options:
                return False
            for i in options:
                metrics[x][y] = i
                if can_fix(x, y):
                    return True
            metrics[x][y] = 0
            return False
        else:
            y += 1
            if y >= 9:
                y = 0
                x += 1
            if x >= 9:
                return True

while True:
    metrics = []
    for _ in range(9):
        metrics.append(list(map(int, input().split())))
    if can_fix(0, 0):
        for row in metrics:
            print(' '.join(list(map(str, a))))

