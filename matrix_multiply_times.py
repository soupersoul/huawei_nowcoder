total_m = [
(50, 10),
(10, 20),
(20, 5)
]
def multiply_times(s):
    i = 0
    matrixes = []
    times = 0
    while i < len(s):
        i+= 1
        if s[i] == '(':
            m, count, used_s_len = multiply_times(s[i:])
            i += used_s_len
            times += count
            matrixes.append(m)
        elif s[i] == ')':
            break
        else:
            matrixes.append(total_m.pop(0))
    m1 = matrixes.pop(0)
    while len(matrixes) > 0:
        m2 = matrixes.pop(0)
        times += m1[0] * m1[1] * m2[1]
        m1 = (m1[0], m2[1])
    return (m1, times, i)
_, times, _ = multiply_times('(A(BC))')
print(times)