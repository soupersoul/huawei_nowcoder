while True:
    try:
        s = input()
        re = ''
        for c in s:
            if c.isdigit():
                re += '*' + c + '*'
            else:
                re += c
        print(re.replace('**', ''))
    except:
        break