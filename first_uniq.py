s = 'aabbccddeeff'
for c in s:
    if s.count(c) == 1:
        print(c)
else:
    print(-1)