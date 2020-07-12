while True:
    try:
        line = input()
        clist = list(line)
        count_dict = {}
        for c in line:
            if c in count_dict:
                count_dict[c] += 1
            else:
                count_dict[c] = 1
        min_count = min(count_dict.values())
        for c in count_dict:
            if count_dict[c] == min_count:
                clist.remove(c)
        print("".join(clist))
    except Exception as e:
        print(e)
        break