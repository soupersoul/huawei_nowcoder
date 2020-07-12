def sort_score(score_list, order):
    if order == 1:
        for i in range(len(score_list)):
            for j in range(0, len(score_list) - i - 1):
                if score_list[j][1] > score_list[j+1][1]:
                    temp = score_list[j]
                    score_list[j] = score_list[j+1]
                    score_list[j+1] = temp
    else:
        for i in range(len(score_list)):
            for j in range(0, len(score_list) - i -1):
                if score_list[j][1] < score_list[j+1][1]:
                    temp = score_list[j]
                    score_list[j] = score_list[j+1]
                    score_list[j+1] = temp

din = [
 'qhsq 15',
'ozslg 79',
'ncttmtsphb 71',
'a 39',
'eeiuyzsj 34',
'nmlrokx 21',
'pjizylo 90',
'ec 45',
'f 12',
'sh 31',
'fm 25',
'ptprphubqk 29',
'wxdiwv 0',
'uhlcpjtxad 60',
'w 20',
'zwktbpun 70',
'efzfkf 69',
'v 31',
'rsnrgtl 73',
'lhdo 76',
'wt 56',
'mcdwd 14',
'ydrnoyd 37',
'gmlfds 76',
'zx 1',
'dqx 98',
'gz 90',
'kvbzrwrrjj 13'

]


score_list = []
order=1
for i in range(len(din)):
    it = din[i].split()
    score_list.append((it[0], int(it[1])))
sort_score(score_list, order)
for item in score_list:
    print('{} {}'.format(item[0], item[1]))