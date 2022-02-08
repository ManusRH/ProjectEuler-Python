# -*- coding: utf-8 -*-
"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""
from eulerlib import is_prime
from itertools import permutations

result = []

for n in range(1000, 10000):
    if is_prime(n) == False:
        continue

    l = list(permutations(list(str(n))))
    pri = []
    for i in l:
        i = int(''.join(i))
        if is_prime(i) and len(str(i)) == 4:
            pri.append(i)

    pri = list(set(pri))

    for a in pri:
        for b in range(1,10000):
             if a + b in pri and a + b * 2 in pri and sorted(pri) not in result:
                 result.append(sorted(pri))

print(result) #second is result
