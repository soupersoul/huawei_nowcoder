
parts = 'gqpj /lrl d:\ a:\ c:\ /nkb'.split()
cmds = []
temp = []
for p in parts:
    if p[0] == '"':
        if p[-1] == '"':
            cmds.append(p[1:-1])
        else:
            temp.append(p[1:])
    elif p[-1] == '"' and p[0] != '"':
        temp.append(p[:-1])
        cmds.append(" ".join(temp))
        temp = []
    elif len(temp) > 0:
        temp.append(p)
    else:
        cmds.append(p)
print(cmds)