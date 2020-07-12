s1 = 'abcdefghijklmnop'
s2 = 'abcsafjklmnopqrstuvw'

if len(s1) > len(s2):
    base = s2
    target = s1
else:
    base = s1
    target = s2

def find_common_str(base, target):
    temp_l = 1
    l = 0
    i = 0
    common_str = ''

    while i < len(base) and i + temp_l <= len(base):
        s = base[i:i+temp_l]
        print(s, i, temp_l)
        if s in target:
            common_str = s
            l = temp_l
            temp_l += 1
        else:
            i += 1
    return common_str

def find_common_str2(base, target):
    m = [['']*(len(target)+1) for _ in range(len(base)+1)]
    re = ''
    for i in range(len(base)):
        for j in range(len(target)):
            if base[i] == target[j]:
                m[i+1][j+1] = m[i][j] + base[i]
                if len(m[i+1][j+1]) > len(re):
                    re = m[i+1][j+1]
    return re
print(find_common_str(base, target))
print(find_common_str2(base, target))