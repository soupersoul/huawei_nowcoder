while True:
    try:
        n = input()
        li = list(map(int, input().split()))
        positive = []
        negative = []
        for i in li:
            if i > 0:
                positive.append(i)
            elif i < 0:
                negative.append(i)
        if positive:
            print(len(negative), '%.1f'%(sum(positive) / len(positive)))
        else:
            print(len(negative), '0.0')
    except:
        break