N, m = map(int, input().strip().split(" "))
N = N // 10
Ni = [[0 for _ in range(4)] for _ in range(m + 1)]
Ri = [[0 for _ in range(4)] for _ in range(m + 1)]
Vi = [0] * (m + 1)
f = [0] * (N + 1)
for i in range(1, m + 1):
    v, p, q = map(int, input().strip().split(" "))
    Vi[i] = v
    v = v // 10
    if q == 0:
        for x in range(4):
            Ni[i][x], Ri[i][x] = v, v * p 
    elif Ni[q][0] == Ni[q][1]:
        Ni[q][1], Ni[q][3] = Ni[q][1] + v, Ni[q][3] + v
        Ri[q][1], Ri[q][3] = Ri[q][1] + v * p, Ri[q][3] + v * p
    else:
        Ni[q][2], Ni[q][3] = Ni[q][2] + v, Ni[q][3] + v
        Ri[q][2], Ri[q][3] = Ri[q][2] + v * p, Ri[q][3] + v * p
minJ = min(Vi) - 1
for i in range(1, m + 1):
    for j in range(N, minJ, -1):
        for k in range(4):
            if j >= Ni[i][k]:
                f[j] = max(f[j], f[j - Ni[i][k]] + Ri[i][k])
print(10 * f[N])