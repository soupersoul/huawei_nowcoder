def max_digit(s):
    if len(s) == 0:
        return None
    maxlen = 0
    di = []
    templen = 0
    temp_str = ''
    for i, c in enumerate(s):
        if c.isdigit():
            templen += 1
            temp_str += c
            if templen > maxlen:
                di = [temp_str]
                maxlen = templen
            elif templen == maxlen:
                di.append(temp_str)
        else:
            templen = 0
            temp_str = ''
    if maxlen > 0:
        return (di, maxlen)
while True:
    try:
        s = input()
        re = max_digit(s)
        if re:
            print(''.join(re[0]) + ',' + str(re[1]))
        else:
            print('')
    except:
        break