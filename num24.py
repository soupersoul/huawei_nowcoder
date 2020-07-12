def trans(num, x):
    print(num, x)
    if len(x) == 1:
        if num == x[0]:
            return True
        else:
            return False
    else:
        re = False
        for i in range(len(x)):
            new_x = x.copy()
            a = new_x.pop(i)
            re = re or trans(num+a, new_x) or trans(num-a, new_x) or trans(num*a, new_x) or trans(num/a, new_x)
        return re

num = 24.0
x = list(map(float, '3 9 3 4'.split()))
if trans(num, x):
    print('true')
else:
    print('false')
