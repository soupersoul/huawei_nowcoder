def gcd(a, b):
    if not b:
        return a
    return gcd(b, a%b)

while True:
    try:
        m, n = map(int, input().split())
        print(m*n // gcd(m, n))
    except:
        break