def dist(s1, s2):
    m = [ [0] * (len(s2)+1) for _ in range(len(s1)+1)]
    for i in range(len(s1)+1):
        m[i][0] = i
    for i in range(len(s2)+1):
        m[0][i] = i
    if s1[0] == s2[0]:
        m[1][1] = 0
    else:
        m[1][1] = 1
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                m[i][j] = m[i-1][j-1]
            else:
                m[i][j] = min(m[i-1][j], m[i][j-1], m[i-1][j-1]) + 1
    return m[len(s1)][len(s2)]

s1 = 'abcdef'
s2 = 'abcdefg'
print(dist(s1, s2))