while True:
    try:
        m, n = map(int, input().split())
        if m > 0 and m <= 9 and n > 0 and n <= 9:
            print(0)
        else:
            print(-1)
        m1,n1, m12, n12 = map(int, input().split())
        if m1 >= 0 and m1 < m and n1 >= 0 and n1 < n and m12 >= 0 and m12 < m and n12 >= 0 and n12 < n:
            print(0)
        else:
            print(-1)
        m2 = int(input())
        if m2 >= 0 and m2 < m:
            print(0)
        else:
            print(-1)
        n2 = int(input())
        if n2 >= 0 and n2 < n:
            print(0)
        else:
            print(-1)
        m3, n3 = map(int, input().split())
        if m3 >= 0 and m3 < m and n3 >= 0 and n3 < n:
            print(0)
        else:
            print(-1)
    except:
        break