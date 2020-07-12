y, m, d = map(int, input().split())
total_day = sum(days[:m-1]) + d
if (y%4 == 0 or y%400 == 0) and m > 2:
    total_day += 1
print(total_day)