while True:
    try:
        n = input()
        line = map(int,raw_input().split())
        maxStep = [1]
        for i in range(1, len(line)):
            res = 1
            for j in range(0, i):
                if line[j] < line[i]:
                    res = max(maxStep[j]+1, res)
            maxStep.append(res)
        print max(maxStep)      
    except:
        break

import bisect
while True:
    try:
        a, b = int(input()), map(int, input().split())
        q = []
        for v in b:
            pos = bisect.bisect_left(q, v)
            if pos == len(q):
                q.append(v)
            else:
                q[pos] = v
        print(len(q))
    except:
        break