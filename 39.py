# -*- coding: utf-8 -*-
#"""
#If p is the perimeter of a right angle triangle with integral
#length sides, {a,b,c}, there are exactly three solutions for p = 120.
#
#{20,48,52}, {24,45,51}, {30,40,50}
#
#For which value of p ≤ 1000, is the number of solutions maximised?
#"""

import math as m

l = []

for a in range(1, 1001):
    for b in range(1, a):
        c = m.sqrt(a**2 + b**2)
        p = a + b + c
        if c % 1 == 0 and p <= 1000:
            l.append(p)

print(max(set(l), key=l.count))
