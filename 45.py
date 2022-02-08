# -*- coding: utf-8 -*-
"""
Triangle, pentagonal, and hexagonal numbers are generated by the
 following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""
triangle = []
pentagonal = []
hexagonal = []

for n in range(2, 80000):
    triangle.append(n*(n+1)/2)
    pentagonal.append(n*(3*n-1)/2)
    hexagonal.append(n*(2*n-1))

l = []

for t in triangle:
    if t in pentagonal and t in hexagonal:
        l.append(t)
    if len(l) > 1:
        break

print(l)
