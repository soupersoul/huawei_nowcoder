def pwd_level(s):
    score = 0
    if len(s) <= 4:
        score += 5
    elif len(s) <= 7:
        score += 10
    else:
        score += 25
    count_i = 0
    count_low = 0
    count_up = 0
    count_other = 0
    for c in s:
        if c.isdigit():
            count_i += 1
        elif c.islower():
            count_low += 1
        elif c.isupper():
            count_up += 1
        else:
            count_other += 1
    if count_i == 1:
        score += 10
    elif count_i > 1:
        score += 20
    if count_low > 0 and count_up > 0:
        score += 20
    elif count_low + count_up > 0:
        score += 10
    if count_other == 1:
        score += 10
    elif count_other > 1:
        score += 25
    if count_i > 0 and count_low > 0 and count_up > 0 and count_other > 0:
        score += 5
    elif count_i > 0 and count_low + count_up > 0 and count_other == 0:
        score += 2
    elif count_i > 0 and count_low + count_up > 0 and count_other > 0:
        score += 3
    return score

while True:
    try:
        s = input()
        score = pwd_level(s)
        if score >= 90:
            print('VERY_SECURE')
        elif score >= 80:
            print('SECURE')
        elif score >= 70:
            print('VERY_STRONG')
        elif score >= 60:
            print('STRONG')
        elif score >= 50:
            print('AVERAGE')
        elif score >= 25:
            print('WEAK')
        else:
            print('VERY_WEAK')
    except:
        break