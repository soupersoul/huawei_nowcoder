while True:
    try:
        i = input()
        asset = input().split()
        re = {}
        for k in asset:
            re[k] = 0
        re['Invalid'] = 0
        j = input()
        tickets = input().split()
        for t in tickets:
            if t in asset:
                re[t] += 1
            else:
                re['Invalid'] += 1
        for k in asset:
            print('{} : {}'.format(k, re[k]))
        print('{} : {}'.format('Invalid', re['Invalid']))
    except:
        break