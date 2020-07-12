def fall(h0, n):
    hi = float(h0)
    si = -hi
    for i in range(n):
        si = si + hi * 2
        hi = hi / 2
    return (si, hi)

print(fall(1, 1))
print(fall(1, 2))
print(fall(1, 3))
print(fall(1, 4))
print(fall(1, 5))
