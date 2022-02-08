"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime
below one-hundred.

The longest sum of consecutive primes below one-thousand that adds
to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the
most consecutive primes?
"""
from eulerlib import primes, is_prime

pri = primes(1000000)

for p in range(0, len(pri)):
    r = 0
    while r < 1000000:
        r += pri[p]
        p += 1
    r -= pri[p-1]
    if is_prime(r):
        print(r)
        break
