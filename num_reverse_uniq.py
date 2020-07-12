while True:
    try:
        istr = input().strip()[::-1]
        re = []
        for i in list(istr):
            if i not in re:
                re.append(i)
        print(re)
    except:
        break