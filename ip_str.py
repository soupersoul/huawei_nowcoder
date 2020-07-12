def ip2int(ip_str):
    parts = ip_str.split(".")
    binstr = ""
    for p in parts:
        binstr += bin(int(p))[2:].rjust(8, "0")
    return int(binstr, 2)

def int2ip(intstr):
    binstr = bin(int(intstr))[2:]
    ip = [0] * 4
    ip[3] = str(int(binstr[-8:], 2))
    ip[2] = str(int(binstr[-16:-8], 2))
    ip[1] = str(int(binstr[-24:-16], 2))
    ip[0] = str(int(binstr[:-24], 2))
    return ".".join(ip)

print(ip2int('10.0.3.193'))
print(int2ip('167969729'))
