def ways(m, n):
    if m < 0 or n < 0:
        return 0
    if m == 1 or n ==1:
        return 1
    else:
        return ways(m, n-1) + ways(m-n, n)

print(ways(7, 3))