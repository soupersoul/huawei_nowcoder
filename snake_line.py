def snake_lines(lines):
    re = [[] for i in range(lines)]
    num = 0
    for i in range(lines):
        for j in range(i+1):
            num += 1
            re[i-j].append(str(num))
    for row in re:
        print(" ".join(row))


lines = 41
snake_lines(lines)
