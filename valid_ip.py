import re
import pdb

A, B, C, D, E, err, pri = (0,0,0,0,0,0,0)
submasks=[254,252,248,240,224,192,128,0]

def format_ip_str(s):
    if re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', s):
        sub_sets = s.split('.')
        if len(sub_sets) != 4:
            return None
        try:
            for ss in sub_sets:
                ip_i = int(ss)
                if ip_i < 0 or ip_i > 255:
                    return None
        except:
            return None
        m = map(int, sub_sets)
        return list(m)
    else:
        return None

def valid_ip(ip_str):
    ips = format_ip_str(ip_str)
    if ips is not None:
        if ips[0] == 0 or ips[0] == 127:
            return None
        else:
            return ips
    return None

def valid_mask(mask_str):
    masks = format_ip_str(mask_str)
    if masks is not None:
        if masks[0] == 255:
            if masks[1] == 255:
                if masks[2] == 255:
                    if masks[3] in submasks:
                        return True
                elif masks[2] in submasks and masks[3] == 0:
                    return True
            elif masks[1] in submasks and masks[2] == 0 and masks[3] == 0:
                return True
        elif masks[0] in submasks and masks[0] != 0 and masks[1] == 0 and masks[2] == 0 and masks[3] == 0:
            return True
    return False

while True:
    line = input().strip()
    if line == "":
        break
    ip_mask = line.split("~")
    ip = valid_ip(ip_mask[0])
    mask = ip_mask[1]
    if ip is not None and valid_mask(mask):
        if ip[0] <= 126:
            A += 1
            if ip[0] == 10:
                pri += 1
        elif ip[0] <= 191:
            B += 1
            if ip[0] == 172 and ip[1] >= 16 and ip[1] <= 31:
                pri += 1
        elif ip[0] <= 223:
            C += 1
            if ip[0] == 192 and ip[1] == 168:
                pri += 1
        elif ip[0] <= 239:
            D += 1
        else:
            E += 1
    else:
        err += 1

print("{} {} {} {} {} {} {}".format(A, B, C, D, E, err, pri))