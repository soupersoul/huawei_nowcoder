def pipeline(s1, s2):
    s = combine(s1, s2)
    s = order(s)
    s = bit_reverse(s)
    return s

def bit_reverse(s):
    rule = "0123456789ABCDEFabcdef"
    re = ''
    for c in s:
        if c in rule:
            int_c = int( c, 16)
            new_c = hex(int(bin(int_c)[2:][::-1].ljust(4, '0'), 2))[2:].upper()
            re += new_c
        else:
            re += c
    return re

def order(s):
    odd_c = []
    even_c = []
    for i in range(len(s)):
        if i%2 == 0:
            even_c.append(s[i])
        else:
            odd_c.append(s[i])
    odd_c.sort()
    even_c.sort()
    re = ''
    for i in range(len(even_c)):
        re += even_c[i]
        if i < len(odd_c):
            re += odd_c[i]
    return re

def combine(s1, s2):
    return s1 + s2

print(pipeline('dec', 'fab'))
