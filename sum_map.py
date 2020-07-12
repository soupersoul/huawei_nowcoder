while True:
    try:
        size = int(input().strip())
        data_map = {}
        for i in range(size):
            (key, value) = tuple(input().strip().split(" "))
            data_map[key] = data_map.get(key, 0) + int(value)
        for k in sorted(data_map.keys()):
            print("{} {}".format(k, data_map[k]))
    except:
        break