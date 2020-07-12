def u(cur, top):
    if len(li) <= 4:
        if cur == 0:
            cur = len(li) - 1
        else:
            cur -= 1
    else:
        if cur == 0:
            if top == 1:
                cur = 3
                top = len(li) - 3
            else:
                top -= 1
        else:
            cur -= 1
    return (cur, top)

def d(cur, top):
    if len(li) <= 4:
        if cur == len(li) -1:
            cur = 0
        else:
            cur += 1
    else:
        if cur == 3:
            if top == len(li)-3:
                cur = 0
                top = 1
            else:
                top += 1
        else:
            cur += 1
    return (cur, top)




n = 81
cmd = 'DDUUUDUUDDUDUUUUDUDDDDDUDUUDDUUDUDDUUUDUUUUUDDDDUDDDUUUDUUUDDDDDUDDDDDUDDDDDUDDUDDDDU'
li = range(1,n+1)
print(cmd.count('U'))
print(cmd.count('D'))
times = cmd.count('U') - cmd.count('D')
print(times)
if times > 0:
    direction = 'U'
else:
    times = 0 - times
    direction = 'D'
print(times)
cur = 0
top = 1
for _ in range(times):
    if direction == 'U':
        cur, top = u(cur, top)
    else:
        cur, top = d(cur, top)
cur_li = []
for i in range(min(4, len(li))):
    cur_li.append(top+i)
print(' '.join(map(str, cur_li)))
print(cur_li[cur])
