"""
How many numbers below fifty million can be expressed as the sum of a
prime square, prime cube, and prime fourth power?
"""
from eulerlib import primes
from math import sqrt
from bisect import insort

def bin_search(n, l):
    start = 0
    end = len(l) - 1

    while start <= end:
        mid_index = (start + end) // 2
        mid_val = l[mid_index]

        if mid_val == n:
            return True#mid_index
        elif n > mid_val:
            start = mid_index + 1
        elif n < mid_val:
            end = mid_index - 1

lim = 50000000

pl = primes(sqrt(lim)+1)

result = 0

mem = []

for a in pl:
    print(a)
    if a**2 > lim: break
    for b in pl:
        if a**2 + b**3 > lim: break
        for c in pl:
            n = a**2 + b**3 + c**4
            if n < lim and not bin_search(n, mem):
                result += 1
                insort(mem, n)
            elif n > lim:
                break

print(result)
