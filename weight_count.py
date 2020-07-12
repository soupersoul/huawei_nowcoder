def count(size, weights, nums):
    sets = set()
    for n in range(nums[0] + 1):
        sets.add(n * weights[0])
    for i in range(1, size, 1):
        last_sets = sets.copy()
        for s in last_sets:
            for n in range(1, nums[i] + 1, 1):
                sets.add(s + n * weights[i])
    return len(sets)

#print(count(2, [1,2], [2,1]))
size_line = '6'
weights_line = '5 133 140 81 73 10'
nums_line = '2 4 6 1 2 6'
size = int(size_line)
weights = list(map(int, weights_line.split()))
nums = list(map(int, nums_line.split()))
print(count(size, weights, nums))
