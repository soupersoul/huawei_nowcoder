while True:
    try:
        n = input()
        l1 = input().split()
        m = input()
        l2 = input().split()
        all_ls = list(map(int, set.union(set(l1), set(l2))))
        all_ls.sort()
        print(''.join(list(map(str, all_ls))))
    except:
        break