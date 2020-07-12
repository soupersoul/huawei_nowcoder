n1 = 100 // 5
n2 = 100 // 3 + 1
for i in range(n1):
    for j in range(n2):
        if 5 * i + 3 * j + (100 - i - j)/3.0 == 100:
            print("{} {} {}".format(i, j, 100-i-j))