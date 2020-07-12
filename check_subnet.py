def valid_format(addr):
    s = addr.split('.')
    if len(s) != 4:
        return None
    try:
        ss = list(map(int, s))
    except:
        return None
    for i in ss:
        if i < 0 or i > 255:
            return None
    return ss

def check_subnet(mask, ip1, ip2):
    m = valid_format(mask)
    print(m)
    i1 = valid_format(ip1)
    print(i1)
    i2 = valid_format(ip2)
    print(i2)
    if not (m and i1 and i2):
        return 1
    r1 = []
    r2 = []
    for i in range(4):
        r1.append(str(i1[i] & m[i]))
        r1.append(str(i2[i] & m[i]))
    if ''.join(r1) == ''.join(r2):
        return 0
    else:
        return 2


mask = '255.255.255.0'
ip1 = '192.168.224.256'
ip2 = '192.168.10.4'
#print(check_subnet(mask, ip1, ip2))
mask1 = '255.0.0.0'
ip11 = '193.194.202.15'
ip21 = '232.43.7.59'
print(check_subnet(mask1, ip11, ip21))

mask2 = '255.0.0.0'
ip12 = '193.194.202.15'
ip22 = '232.43.7.59'
#print(check_subnet(mask1, ip11, ip21))