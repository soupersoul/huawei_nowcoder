def check_len(s):
    return len(s) > 8

def check_chr_type(s):
    up, lo, di, ot = 0, 0, 0, 0
    for c in s:
        if c.isupper():
            up = 1
        elif c.islower():
            lo = 1
        elif c.isdigit():
            di = 1
        else:
            ot = 1
    return (up + lo + di + ot) >= 3

def check_duplicate(s):
    for i in range(len(s) - 3):
        if s.count(s[i:i+3]) > 1:
            return False
    return True

while True:
    try:
        s = input().strip()
        if check_len(s) and check_chr_type(s) and check_duplicate(s):
            print("OK")
        else:
            print("NG")
    except Exception as e:
        print(e)
        break