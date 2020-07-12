n = 2000
count = 0
for i in range(1, n+1):
    x = i * i
    s = str(i)
    l = len(s)
    if s == str(x)[-l:]:
        count += 1
print(count)