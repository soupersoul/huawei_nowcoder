def getVal(x):
    if x == 'J':
        return 11
    elif x == 'Q':
        return 12
    elif x == 'K':
        return 13
    elif x == 'A':
        return 1
    else:
        return int(x)
def trans(num, li):
    if len(li) == 1:
        if num == getVal(li[0]):
            re[0] = li[0]
            return True
        else:
            return False
    else:
        for i in range(len(li)):
            new_li = li.copy()
            x = new_li.pop(i)
            l = len(new_li)
            if trans(num+getVal(x), new_li):
                re[l] = '-{}'.format(x)
                return True
            if trans(num-getVal(x), new_li):
                re[l] = '+{}'.format(x)
                return True
            if trans(num * getVal(x), new_li):
                re[l] = '/{}'.format(x)
                return True
            if trans(num / getVal(x), new_li):
                re[l] = '*{}'.format(x)
                return True

s = 'A A A A'
d = s.split()
re = [''] * 4
if 'joker' in d or 'JOKER' in d:
    print('ERROR')
else:
    if trans(24, d):
        print(''.join(re))
    else:
        print('NONE')
