"""
Find the sum of the distinct squarefree numbers in
the first 51 rows of Pascal's triangle.
"""
from math import factorial, sqrt

def nCr(n,r):
    return int(factorial(n) / (factorial(r)*factorial(n-r)))

def primeFactors(n):
    result = []

    while n % 2 == 0:
        result.append(2)
        n = n / 2
    for i in range(3, int(sqrt(n))+2, 2):
        while n % i == 0:
            result.append(i)
            n = n / i
    if n > 2:
        result.append(int(n))
    return result

lim = 8

pascal = [1]

for n in range(lim):
    for r in range(n+1):
        p = nCr(n, r)
        if p not in pascal:
            pascal.append(p)

pascal = list(set(pascal))

final = 0

for d in pascal:
    pf = primeFactors(d)
    if sorted(list(set(pf))) == pf:
        final += d

print(final)
























###############################################################################
