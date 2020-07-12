#s = input()
def sort_char(s):
    re = list(s)
    s1 = filter(lambda c: c.isalpha(), list(s))
    sort_s = list(s1)
    sort_s.sort(key=str.upper)
    j = 0
    for i in range(len(s)):
        if re[i].isalpha():
            re[i] = sort_s[j]
            j += 1
    print(''.join(re))


sort_char("Type")
sort_char("BabA")
sort_char("By?e")
sort_char("A Famous Saying: Much Ado About Nothing (2012/8).")