"""
It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""
from itertools import permutations

found = False
n = 100

while not found:
    p = [int(x) for x in ["".join(x) for x in list(permutations(str(n)))]]
    yes = 1
    for x in range(2,7):
        if n*x in p:
            yes += 1
    if yes >= 6:
        print(n)
        break
    n += 1