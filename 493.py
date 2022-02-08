"""
70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.

What is the expected number of distinct colors in 20 randomly picked balls?

Give your answer with nine digits after the decimal point (a.bcdefghij).
"""
from math import factorial

def choose(n,m):
    return factorial(n)/(factorial(m)*factorial(n-m))


print(7*(1-(choose(60,20)/choose(70,20))))
