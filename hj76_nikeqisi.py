n=6

def cube_odd(n):
    x = n ** 2 - n +1
    re = []
    for i in range(n):
        re.append(str(x + i * 2))
    print('+'.join(re))

cube_odd(6)