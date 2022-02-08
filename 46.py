# -*- coding: utf-8 -*-
"""
It was proposed by Christian Goldbach that every odd composite
number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the
sum of a prime and twice a square?
"""
from eulerlib import primes

pri = primes(10000)

n = 3

while True:
    found = 0
    p = 0
    while n >= pri[p]:
        s = 0
        while n >= pri[p] + 2*s**2:
            if pri[p] + 2*s**2 == n:
                found += 1
            s += 1
        p += 1
    if found == 0:
        print(n)
        break
    n += 2
