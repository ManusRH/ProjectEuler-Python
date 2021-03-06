"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =   
n!
r!(n−r)!
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100,
 are greater than one-million?
"""
def fac(n):
    if n == 1: return 1
    else: return n*fac(n-1)

def choose(n, r):
    return int(fac(n) / (fac(r)*fac((n-r))))

result = 0

for n in range(22, 101):
    for r in range(2, n):
        if choose(n,r) > 1000000:
            result += 1

print(result)
