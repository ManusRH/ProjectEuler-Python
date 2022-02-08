"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

d = ""

for i in range(1, 1000001):
    for e in str(i):
        d += e

d1 = int(d[1 - 1])
d10 = int(d[10 - 1])
d100 = int(d[100 - 1])
d1000 = int(d[1000 - 1])
d10000 = int(d[10000 - 1])
d100000 = int(d[100000 - 1])
d1000000 = int(d[1000000 - 1])


print(d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000)

