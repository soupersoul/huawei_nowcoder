def match(st, rstr):
    lr = len(rstr)
    ls = len(st)
    dp = [ [False for _ in range(ls+1)] for _ in range(lr+1)]
    dp[0][0] = True
    if rstr[0] == '*':
        dp[1][0] = True
        dp[1][1] = True
    if rstr[0] == '?':
        dp[1][1] = True
    for i in range(1, lr+1):
        for j in range(1, ls+1):
            if rstr[i-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            elif rstr[i-1] == '?':
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] and rstr[i-1] == st[j-1]
    return dp[lr][ls]

s1 = 'te?t*.*'
s2 = 'txt12.xls'

if match(s1, s2):
    print('true')
else:
    print('false')