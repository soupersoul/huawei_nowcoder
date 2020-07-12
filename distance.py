def count_dist(a, b):
    len_a = len(a)
    len_b = len(b)
    x = [[0 for j in range(len_b)] for i in range(len_a)]
    for j in range(len_b):
        x[0][j] = j
    for i in range(len_a):
        x[i][0] = i
    if a[0] == b[0]:
        x[0][0] = 0
    else:
        x[0][1] = 1
        x[1][0] = 1
        x[0][0] = 1
    for i in range(1,len_a):
        for j in range(1,len_b):
            if a[i-1] == b[j-1]:
                x[i][j] = x[i-1][j-1]
            else:
                x[i][j] = min(x[i-1][j], x[i][j-1], x[i-1][j-1]) + 1
    print(x[-1][-1])


a = 'abcdefg'
b = 'abcdef'
count_dist(a, b)
