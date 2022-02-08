"""
Find the least value of n for which the remainder first exceeds 10^10.
"""
from eulerlib import primes

pri = primes(10000000)
n = 1

for p in pri:
    print(n)
    m = (pow(p-1, n) + pow(p+1, n)) % pow(p, 2)
    if m > 10**10:
        print("Found:", n)
        break
    n += 1
