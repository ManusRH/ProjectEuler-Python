"""
If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).
"""
from numpy import prod

def rad(n):
    i = 2
    r = []
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i
            r.append(i)
    if n > 1:
        r.append(n)
    return prod(list(set(r)))

result = []

for n in range(1, 100001):
    rn = rad(n)
    result.append((rn,n))

result = sorted(result)

print(result[10000 - 1][1])
