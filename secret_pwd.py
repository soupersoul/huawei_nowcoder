a1 = 'abcdefghijklmnopqrstuvwxyz'
a2 = '22233344455566677778889999'
mapping = dict(zip(list(a1), list(a2)))
def translate_up(c):
    return chr(ord(c) + 1).lower()

while True:
    try:
        s = input()
        re = ""
        for c in s:
            if c.isupper():
                re += translate_up(c)
            elif c.islower():
                re += mapping[c]
            else:
                re += c
        print(re)
    except EOFError as ee:
        print(ee)
        break
    except Exception as e:
        print(e)
        break
