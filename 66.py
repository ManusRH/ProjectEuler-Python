"""
Consider quadratic Diophantine equations of the form:

x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is
649^2 – 13×180^2 = 1.

Find the value of D ≤ 1000 in minimal solutions of x
for which the largest value of x is obtained.
"""
from math import sqrt, floor
from fractions import Fraction
from decimal import getcontext, Decimal

getcontext().prec = 500

def find_period(n):
    n = Decimal(n).sqrt()
    a0 = floor(n)
    if n - a0 == 0: return 0
    period = [a0]
    while period[-1] != a0*2:
        n = (n - floor(n))**(-1)
        period.append(floor(n))
    return period

def convergents(p, n, i=0, t=True):
    if t:
        return p[0] + Fraction(1, convergents(p, n-1, i+1, t=False))
    try:
        p[i]
    except:
        i = 1
    if n == 0:
        return p[i]
    return p[i] + Fraction(1, convergents(p, n-1, i+1, t=False))

result = []

for D in range(1,1001):
    if sqrt(D) % 1 == 0:
        continue
    n = 1
    while True:
        x = convergents(find_period(D), n).numerator
        y = convergents(find_period(D), n).denominator
        if x**2 - D*y**2 == 1:
            result.append((x, D))
            break
        n += 1
    #print(D)

print(max(result))
