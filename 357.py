"""
Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d+n/d is prime.
"""
from eulerlib import is_prime, primes
from math import sqrt

result = 0
lim = 100000000
pri = primes(lim)

for n in pri:
    n -= 1
    d = 2
    while d < sqrt(n):
        if n%d == 0:
            if not is_prime(d+n//d):
                break
        d += 1
    else:
        if is_prime(n+1):
            result += n
            print(n)

print()
print(result-4)
