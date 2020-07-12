import re
mp = {
    '1': '壹',
    '2': '贰',
    '3': '叁',
    '4': '肆',
    '5': '伍',
    '6': '陆',
    '7': '柒',
    '8': '捌',
    '9': '玖'
}

level = ['', '拾', '佰', '仟']

def level_qian(s):
    if not s or int(s) == 0:
        return ''
    r = ''
    l = len(s)
    for i in range(l):
        if s[i] == '0' and i < 3:
            r += '零'
        else:
            r += mp[s[i]] + level[l-i-1]
    return re.sub('零+', '零', r).replace('壹拾', '拾')

def read_rmb(rmb):
    (yuan, jiaofen) = rmb.split('.')
    re = '人民币'
    if yuan != '0':
        if len(yuan) > 8:
            re += level_qian(yuan[:-8]) + '亿'
        part = yuan[-8:-4]
        wan = level_qian(part)
        if wan:
            re += wan + '万'
        part = yuan[-4:]
        re += level_qian(part) + '元'

    if int(jiaofen) != 0:
        if jiaofen[0] != '0':
            re += mp[jiaofen[0]] + '角'
        if jiaofen[1] != '0':
            re += mp[jiaofen[1]] + '分'
    else:
        re += '整'
    return re

print(read_rmb('532.00'))
print(read_rmb('6007.14'))
print(read_rmb('151121.15'))
print(read_rmb('13.64'))