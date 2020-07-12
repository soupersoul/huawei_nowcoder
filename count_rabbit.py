# 第3个月起，即满2个月
def count_month(n):
    if n < 3:
        return 1
    return count_month(n-1) + count_month(n-2)


def count_month2(month):
    if month<3:
        return 1
    else:
        a=1
        b=1
        for i in range(3,month+1):
            a,b=b,a+b
        return b

print(count_month(3))
print(count_month(4))
print(count_month(5))
print(count_month(6))
print(count_month(9))

print(count_month2(3))
print(count_month2(4))
print(count_month2(5))
print(count_month2(6))
print(count_month2(9))