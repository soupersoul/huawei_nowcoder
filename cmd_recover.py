cmd_map_single = {
    'reset':'reset what',
}

cmd_map_complex = {
    'reset board':'board fault',
    'board add': 'where to add',
    'board delet': 'no board at all',
    'reboot backplane': 'impossible',
    'backplane abort': 'install first',
}

def exec_cmd(cmd_str):
    cmd = cmd_str.split()
    if len(cmd) == 1:
        for key in cmd_map_single.keys():
            if cmd[0] in key:
                return cmd_map_single[key]
        else:
            return 'unkown command'
    elif len(cmd) == 2:
        match_key = []
        for key in cmd_map_complex.keys():
            ks = key.split()
            if cmd[0] in ks[0] and cmd[1] in ks[1]:
                match_key.append(key)
        if len(match_key) == 1:
            return cmd_map_complex[match_key[0]]
        else:
            return 'unkown command'

print(exec_cmd('reset'))
print(exec_cmd('reset board'))
print(exec_cmd('board add'))
print(exec_cmd('board delet'))
print(exec_cmd('reboot backplane'))
print(exec_cmd('backplane abort'))