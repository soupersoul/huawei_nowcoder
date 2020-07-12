def getCode(ori):
    o = 'abcdefghijklmnopqrstuvwxyz'
    unduplicate = ''
    for c in ori.lower():
        if c not in unduplicate:
            unduplicate += c
    for c in o:
        if c not in unduplicate:
            unduplicate += c
    return unduplicate

def encode(raw, code):
    re = ''
    for c in raw:
        cc = code[ord(c.lower()) - ord('a')]
        if c.isupper():
            re += cc.upper()
        else:
            re += cc
    return re

while True:
    try:
        lineCode, line = input(), input()
        code = getCode(lineCode)
        print(encode(line, code))
    except:
        break
