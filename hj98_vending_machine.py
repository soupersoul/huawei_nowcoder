things_nums = [0] * 6
moneys = [0] * 4
left = [0]
valid_money = [1, 2, 5, 10]
valid_thins = ['A1','A2','A3','A4','A5','A6']
price = [2,3,4,5,8,6]
def do_init(param):
    tn = param[0].split('-')
    for i in range(len(tn)):
        things_nums[i] = int(tn[i])
    mn = param[1].split('-')
    for i in range(len(mn)):
        moneys[i] = int(mn[i])
    print('S001:Initialization is successful')

def do_money(m):
    if m not in valid_money:
        print('E002:Denomination error')
    elif m > 2 and moneys[0] + moneys[1] * 2 < m:
        print(moneys)
        print('E003:Change is not enough, pay fail')
    #elif m + left[0] > 10:
    #    print("E004:Pay the balance is beyond the scope biggest")
    elif sum(things_nums) == 0:
        print("E005:All the goods sold out")
    else:
        i = valid_money.index(m)
        moneys[i] += 1
        left[0] += m
        print("S002:Pay success,balance={}".format(left[0]))

def do_buy(x):
    if x not in valid_thins:
        print("E006:Goods does not exist")
    else:
        i = valid_thins.index(x)
        if things_nums[i] == 0:
            print("E007:The goods sold out")
        elif left[0] < price[i]:
            print("E008:Lack of balance")
        else:
            things_nums[i] -= 1
            left[0] -= price[i]
            print("S003:Buy success,balance={}".format(left[0]))

def do_back():
    if left[0] == 0:
        print("E009:Work failure")
    else:
        backs = [0] * 4
        for i in range(len(valid_money)):
            n = left[0]//valid_money[i]
            if n > 0:
                backs[i] = min(n, moneys[i])
            left[0] = left[0] - valid_money[i] * backs[i]
            if left[0] == 0:
                break
        for i in range(4):
            print("{} yuan coin number={}".format(valid_money[i], backs[i]))

def do_query(t):
    if t == '0':
        for i in range(len(valid_thins)):
            print("{} {} {}".format(valid_thins[i], price[i], things_nums[i]))
    elif t == '1':
        for i in range(len(valid_money)):
            print("{} yuan coin number={}".format(valid_money[i], moneys[i]))
    else:
        print("E010:Parameter error")



#cmds = input().split(';')
cmds = 'r 25-9-1-1-12-20 7-3-8-14;p 10;p 10;b A3;c;b A1;q0;p 10;p 5;c;p 1;b A5;q0;'[:-1].split(';')
for c in cmds:
    cm = c.split()

    if cm[0] == 'r':
        do_init(cm[1:])
    elif cm[0] == 'p':
        do_money(int(cm[1]))
    elif cm[0] == 'b':
        do_buy(cm[1])
    elif cm[0] == 'c':
        do_back()
    elif cm[0] == 'q':
        do_query(cm[1])
