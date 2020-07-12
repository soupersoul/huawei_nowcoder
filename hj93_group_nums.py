def have_sum(summ, li):
    if summ == 0:
        return True
    for i in range(len(li)):
        new_li = li.copy()
        x = new_li.pop(i)
        if have_sum(summ - x, new_li):
            return True
    return False

while True:
    try:
        n = input()
        nums = list(map(int, input().split()))
        list5 = []
        list3 = []
        left = []
        for i in nums:
            if i%5 == 0:
                list5.append(i)
            elif i%3 == 0:
                list3.append(i)
            else:
                left.append(i)
        diff = abs(sum(list5) - sum(list3))
        little_double = sum(left) - diff
        if little_double % 2 != 0:
            print('false')
        else:
            summ = little_double / 2
            if have_sum(summ, left):
                print('true')
            else:
                print('false')
    except:
        break