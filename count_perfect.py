def isperfect(n):
    factors = [1]
    for i in range(2, n):
        if i * i > n:
            break
        if n%i == 0:
            factors.append(i)
            factors.append(n/i)
    return sum(factors) == n

def find(n):
    count = 0
    for i in range(2, n+1):
        if isperfect(i):
            count += 1
    return count


while True:
    try:
        n = int(input())
        print(find(n))
    except:
        break