"""
The number, 197, is called a circular prime because all
rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
from eulerlib import primes

primes_list = primes(1000000)

n = 0

for prime in primes_list:
    lp = list(str(prime))
    rot = []
    for i in range(0, len(lp)):
        rot.append(int(''.join(lp[i:] + lp[:i])))
    if all((x in primes_list) for x in rot):
        n += 1

print(n)
