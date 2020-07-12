def max_bottle(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    nl = n % 3
    new = n // 3
    return new + max_bottle(nl + new)

while True:
    try:
        left = int(input())
        print(max_bottle(left))
    except Exception as e:
        print(e)
        break
