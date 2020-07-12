import ntpath



re = {}
fn_sets = []
while True:
    line = input().strip()
    if line == "":
        break
    sets = line.split()
    fn = ntpath.basename(sets[0])
    if len(fn) > 16:
        fn = fn[-16:]
    key = fn + "-" + sets[1]
    if key in fn_sets:
        re[key] += 1
    else:
        fn_sets.append(key)
        re[key] = 1
fn_sets = fn_sets[-8:]
for fn in fn_sets:
    key = fn.split("-")
    print("{} {} {}".format(key[0], key[1], re[fn]))
