"""
How many fractions lie between 1/3 and 1/2 in the sorted 
set of reduced proper fractions for d ≤ 12,000?
"""
from decimal import *

getcontext().prec = 100

result = []

upper = Decimal(1) / Decimal(2)
lower = Decimal(1) / Decimal(3)

for d in range(12001):
    for n in range(d):
        k = Decimal(n) / Decimal(d)
        if lower < k < upper:
            result.append(k)
    print(d)

print(len(set(result)))

# Super duper slow, uses hella much memory and takes 100 seconds
# At least it works
# Answer 7295372