"""
The cube, 41063625 (345^3), can be permuted to produce two other
cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625
is the smallest cube which has exactly three permutations of its
digits which are also cube.

Find the smallest cube for which exactly five permutations of
its digits are cube.
"""
from itertools import permutations

cubes = []

c = 10

result = []

while len(result) < 5:
    b = sorted([int(x) for x in str(c**3)])
    cubes.append(b)
    if cubes.count(b) > 4:
        r = b
        while len(result) < 5:
            b = sorted([int(x) for x in str(c**3)])
            if b == r:
                result.append(c**3)
            c -= 1
    c += 1

print(min(result))
