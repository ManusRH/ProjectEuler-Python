"""
Find the smallest member of the longest amicable chain
with no element exceeding one million.
"""

import math

def divs(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

nums = list(range(1,10**6))

longest = (0,0)

for i in nums:
    print(i, longest)
    initial = i
    length = 1
    next_num = sum(list(divs(initial))[0:-1])
    if next_num == initial:
        del nums[nums.index(i)]
        continue
    else:
        while next_num != initial:
            length += 1
            if next_num not in nums:
                break
            del nums[nums.index(next_num)]
            next_num = sum(list(divs(next_num))[0:-1])
    if length > longest[0]:
        longest = (length, initial)

print(longest)

# answer is 14316, it takes like 10 hours

"""

memor = []
chains = []
ns = list(range(1,10**6))
k = 0

for n in ns:
    print(n)
    chain = [n]
    if sum(list(divs(n))[0:-1]) <= n: 
        del ns[k]
        k += 1
        continue
    while (chain[0] != chain[-1] or len(chain) == 1):
        if n > 10**6 or n == sum(list(divs(n))[0:-1]) or n not in ns:
            break

        n = sum(list(divs(n))[0:-1])
        chain.append(n)
        try:
            del ns[k]
        except: pass
    if chain[0] == chain[-1]:
        chains.append(chain)
    k += 1

result = []

for chain in chains:
    nex = False
    for c in chain:
        if c > 10**6:
            nex = True
            break
    result.append((len(chain), min(chain)))

print(max(result))

"""
