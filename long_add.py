def long_add(s1, s2):
    l = max(len(s1), len(s2))
    s1 = s1.rjust(l, '0')
    s2 = s2.rjust(l, '0')
    extra = 0
    re = []
    for i in range(l-1, -1, -1):
        temp = int(s1[i]) + int(s2[i]) + extra
        if temp > 9:
            extra = temp//10
            temp = temp%10
        else:
            extra = 0
        re.append(str(temp))
    if extra > 0:
        re.append(str(extra))
    re.reverse()
    return ''.join(re)

s1 = '99999999999999999999999999999999999999999999999999'
s2 = '1'
print(long_add(s1, s2))