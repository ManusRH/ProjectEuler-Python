"""
The number 3797 has an interesting property. Being prime itself,
it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. Similarly 
we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable 
from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
from eulerlib import primes

primes = primes(800000)
truncatable = []

n = 4

def lr(prime):
    cont = False
    p = prime
    for lr in range(len(p)):
        for i in range(lr):
            p = p[1:]
            if len(p) == 0:
                continue
            if int(p) not in primes:
                cont = True
    if cont:
        return False
    else:
        return True

def rl(prime):
    cont = False
    p = prime
    for rl in range(len(p)):
        for i in range(rl):
            p = p[:-1]
            if len(p) == 0:
                continue
            if int(p) not in primes:
                cont = True 
    if cont:
        return False
    else:
        return True

while len(truncatable) != 11:
    p = str(primes[n])

    if lr(p) and rl(p):
        truncatable.append(int(p))
        print(truncatable)

    n += 1

print(sum(truncatable))
