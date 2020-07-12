primes = [2, 3]

def make_prime_list(ceil):
    max_done_prime = primes[-1]
    if max_done_prime >= ceil:
        return
    for i in range(max_done_prime + 2, ceil + 2, 2):
        if is_prime(i):
            primes.append(i)

def is_prime(x):
    if x in primes:
        return True
    for p in primes:
        if p * p > x:
            return True
        if x % p == 0:
            return False
    return True

def group_nums(nums):
    evens = []
    odds = []
    for n in nums:
        if n % 2 == 0:
            evens.append(n)
        else:
            odds.append(n)
    return (odds, evens)

def prime_cp_matrics(odds, evens):
    # matrics=[[0] * len(evens)] * len(odds))
    # 这种写法由于[0] * len(evens)] 是一个对象，导致所有的行都指向同一个对象
    matrics=[[0 for i in range(len(evens))]for i in range(len(odds))]
    for i, even in enumerate(odds):
        for j, odd in enumerate(evens):
            if is_prime(even + odd):
                matrics[i][j] = 1
    return matrics

def find_cp(odd_i):
    for even_j in range(len(evens)):
        if matrics[odd_i][even_j] == 1 and used[even_j] == 0:
            used[even_j] = 1
            if cp_list[even_j] == -1 or find_cp(cp_list[even_j]) == 1:
                cp_list[even_j] = odd_i
                return 1
    return 0

size = 22
nums = list(map(int, '20923 22855 2817 1447 29277 19736 20227 22422 24712 27054 27050 18272 5477 27174 13880 15730 7982 11464 27483 19563 5998 16163'.split()))
(odds, evens) = group_nums(nums)
make_prime_list(30000)
matrics = prime_cp_matrics(odds, evens)
count = 0
cp_list = [-1] * len(evens)
for i in range(len(odds)):
    used = [0] * len(evens)
    if find_cp(i):
        count += 1
print(count)
