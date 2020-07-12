primes = [2, 3]

def is_prime(odd_n):
    if odd_n%2 == 0:
        return False
    if odd_n in primes:
        return True
    for p in primes:
        if p ** 2 > odd_n:
            return True
        if odd_n%p == 0:
            return False
    else:
        return True


def make_primes(n):
    if primes[-1] >= n:
        return
    for i in range(3, n, 2):
        if is_prime(i):
            primes.append(i)

while True:
    n = int(input())
    make_primes(n)
    for i in range(n//2, n):
        print(i)
        if is_prime(i) and is_prime(n-i):
            print(n-i)
            print(i)
            break
