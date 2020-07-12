while True:
    try:
        N=int(input())
        if N<=0:
            print(-1)
        else:
            print((3*N+1)*N//2)
    except:
        break