# -*- coding: utf-8 -*-
"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors
each. What is the first of these numbers?
"""
from eulerlib import is_prime

def find_factors(n):
    factors = []
    d = 2
    while n != 1:
        if n % d == 0:
            if is_prime(d):
                factors.append(d)
            n /= d
        else:
            d += 1
    return factors

result = []

n = 1

while len(result) < 4:
    nf = find_factors(n)
    if len(set(nf)) == 4:
        result.append(n - len(result))
    if len(set(result)) > 1:
        result = []
        n -= 1
    print(n)
    n += 1

print("Answer =", result[0])
