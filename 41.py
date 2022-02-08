"""
We shall say that an n-digit number is pandigital if it makes 
use of all the digits 1 to n exactly once. For example, 2143 is 
a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
from itertools import permutations
from eulerlib import is_prime

per9 = reversed(list(permutations([1,2,3,4,5,6,7,8,9])))
per8 = reversed(list(permutations([1,2,3,4,5,6,7,8])))
per7 = reversed(list(permutations([1,2,3,4,5,6,7])))
per6 = reversed(list(permutations([1,2,3,4,5,6])))
per5 = reversed(list(permutations([1,2,3,4,5])))
per4 = reversed(list(permutations([1,2,3,4])))
per3 = reversed(list(permutations([1,2,3])))
per2 = reversed(list(permutations([1,2])))
# Dumb way, i know, but it works

perx = [per9,per8,per7,per6,per5,per4,per3,per2]

found = False

for px in perx:
    for p in px:
        p = int(''.join([str(x) for x in p]))
        if is_prime(p):
            print(p)
            found = True
            break

    if found:
        break

