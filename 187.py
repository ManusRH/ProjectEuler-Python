"""
How many composite integers, n < 10**8, have precisely two,
not necessarily distinct, prime factors?
"""
from eulerlib import primes

lim = 10**8

pri = primes(lim/2)

n = 0

for r1 in range(len(pri)):
    p1 = pri[r1]
    for r2 in range(r1, len(pri)):
        p2 = pri[r2]
        if p1*p2 > lim: break
        n += 1

print("Success:", n)
