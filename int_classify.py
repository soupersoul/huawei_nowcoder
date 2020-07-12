import traceback

try:
    arr_i = "24 7907 610 4359 55 812 3002 10706 2470 8332 8573 3840 8105 9213 10159 11882 6517 7357 6398 4586 215 3420 4927 7159 9414".split(" ")[1:]
    in_r = map(int, "10 85 122 46 55 110 47 77 119 50 58".split(" ")[1:])
    arr_r = sorted(list(set(in_r)))
    re = ["0"]
    total = 0
    for r in arr_r:
        count = 0
        mat = []
        for i, t in enumerate(arr_i):
            if str(r) in t:
                count += 1
                mat.append(str(i))
                mat.append(str(t))
        if count > 0:
            re.append(str(r))
            re.append(str(count))
            re += mat
    if len(re) > 1:
        re[0] = str(len(re) - 1)
    print(" ".join(re))
except Exception as e:
    print(e)
    traceback.print_exc()


while True:
    try:
        s1 = input().split()[1:]
        s2 = list(set(map(int, input().split()[1:])))
        s2.sort()
        rst = []
        for num in s2:
            tmp = []
            for i, sub in enumerate(s1):
                if str(num) in sub:
                    tmp.extend([str(i), str(sub)])
            if tmp:
                rst.extend([str(num), str(len(tmp)//2)] + tmp)
        print(str(len(rst)) + " " + " ".join(rst))
    except:
        break