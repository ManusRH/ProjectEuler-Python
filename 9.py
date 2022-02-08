"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math

a = 1
found = False
while not found:
	for b in range(1,a):
		c = a**2 + b**2
		c2 = math.sqrt(c)
		if a + b + c2 == 1000:
			print(a*b*c2)
			found = True
	a += 1
