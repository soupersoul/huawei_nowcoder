from collections import Counter
lines=['zhangsan', 'lisi']


def score(s):
    cs = Counter(list(s))
    sort_c = sorted(cs.items(), key=lambda x: x[1], reverse=True)
    weights = list(reversed(range(1, 27)))
    score = 0
    for i in range(len(sort_c)):
        score += sort_c[i][1] * weights[i]
    return score

for l in lines:
    print(score(l))