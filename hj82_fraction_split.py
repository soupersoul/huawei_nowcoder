while True:
    try:
        a, b = input().split('/')
        re = []
        while a!=1:
            if b%(a-1) == 0:
                if b//(a-1) < b:
                    re.append('1/{}'.format(b//(a-1)))
                    re.append('1/{}'.format(b))
                else:
                    re.append('1/{}'.format(b))
                    re.append('1/{}'.format(b//(a-1)))
                break
            else:
                q = b // a
                r = b % a
                re.append('1/{}'.format(q+1))
                a = a-r
                b = b(q+1)
        print('+'.join(re))
    except:
        break