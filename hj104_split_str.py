while True:
    try:
        n = int(input())
        for i in range(n):
            s = input()
            while len(s) > 8:
                print(s[0:8])
                s = s[8:]
            print(s.ljust(8, '0'))
    except:
        break