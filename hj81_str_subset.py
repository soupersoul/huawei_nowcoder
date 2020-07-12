while True:
    try:
        s1, s2 = input(), input()
        if set(s1).issubset(set(s2)):
            print('true')
        else:
            print('false')
    except:
        break