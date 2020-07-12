s = '我ABC汉DEF'
size=6
re = ''
count = 0
for c in s:
    print(len(c.encode()))
    if count + len(c.encode()) <= size:
        count += len(c.encode())
        re += c
    else:
        break
print(re)
