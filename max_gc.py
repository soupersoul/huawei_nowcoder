def find_max(s, l):
    max_cnt = 0
    re = ''
    if l >= len(s):
        return s.count('G') + s.count('C')
    for i in range(len(s)-l):
        subs = s[i:i+l]
        new_count = subs.count('G') + subs.count('C')
        if new_count > max_cnt:
            max_cnt = new_count
            re = subs
    return re

s = 'CCCAAGTCTTCCAATCGTGCCCCCCAATTGAGTCTCGCTCCCCAGGTGAGATACATCAGAAGC'
l = 63
print(find_max(s,l))