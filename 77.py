"""
It is possible to write five as a sum in exactly
six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written
as a sum of at least two positive integers?
"""
from eulerlib import primes

p = primes(100000)

k = 10

found = False

while not found:
    result = [1] + [0]*k

    n = 0
    while p[n] < k:
        for i in range(p[n], k+1):
            result[i] += result[i-p[n]]
        n += 1

    if result[k] > 5000:
        print(k)
        found = True

    k += 1
