
def goto(start, end):
    if start[0] == end[0] and start[1] == end[1]:
        paths.append(start)
        return start
    if start[0] + 1 < row and metrics[start[0] + 1][start[1]] == 0 and goto((start[0]+1, start[1]), end):
        paths.append(start)
        return start
    else:
        metrics[start[0] + 1][start[1]] == 1
    if start[1] + 1 < col and metrics[start[0]][start[1] + 1] == 0 and goto((start[0], start[1] + 1), end):
        paths.append(start)
        return start
    else:
        metrics[start[0]][start[1] + 1] == 1
    return None

while True:
    try:
        metrics = []
        paths = []
        (row,col) = tuple(list(map(int, input().split())))
        for i in range(row):
            metrics.append(list(map(int, input().split())))
        goto((0,0), (row-1, col-1))
        paths.reverse()
        for cell in paths:
            print(cell)
    except:
        break
