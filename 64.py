"""
How many continued fractions for N ≤ 10000 have an odd period?
"""
import math as m
import decimal as d

d.getcontext().prec = 500

def find_period_number(n):
    n = d.Decimal(n).sqrt()
    a0 = m.floor(n)
    if n - a0 == 0: return 0

    period = [a0]
    while period[-1] != a0*2:
        n = (n - m.floor(n))**(-1)
        period.append(m.floor(n))
    return len(period)-1

result = 0
lim = 10001

for n in range(lim):
    if find_period_number(n) % 2 == 1:
        result += 1
        print(n, result)

print(result)


