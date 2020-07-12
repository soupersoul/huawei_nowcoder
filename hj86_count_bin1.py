n = int(raw_input())
n2 = bin(n)[2:]
li = range(len(n2))
li.reverse()
for i in li:
    s = '1' * (i+1)
    if s in n2:
        print len(s)
        break

def count_1(bins):
    m = 0
    start = 0
    for i in range(len(bins)):
        if bins[i] == '1':
            if m == 0:
                m = 1
            elif bins[i-m:i+1].count('1') == (m + 1):
                m += 1
    return m

while True:
    try:
        bins = bin(int(input()))
        print(count_1(bins[2:]))
    except:
        break
