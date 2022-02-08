"""
It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
"""
import math
import decimal

sum_of_all = []
decimal.getcontext().prec = 100
sum_int = []

for e in range(1, 100):
    if math.sqrt(e) % 1 != 0:
        sum_of_all.append(list(str(decimal.Decimal(e).sqrt())))

for i in sum_of_all:
    for j in i:
        if j != ".":
            sum_int.append(int(j))

print(sum(sum_int))

# This shit is not accurate at all: the real answer is 40886
