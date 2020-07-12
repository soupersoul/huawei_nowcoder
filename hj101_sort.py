while True:
    try:
        n = input()
        li = list(map(int, input().split()))
        order = int(input())
        print(" ".join(list(map(str, sorted(li, reverse=(order==1))))))
    except:
        break
