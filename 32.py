"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 
1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing 
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be 
written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include 
it once in your sum.
"""

result_list = []

for p in range(1, 10000):
    for m in range(1, p):
        m2 = p/m
        if m2 % 1 != 0:
            continue
        m2 = int(m2)
        digits = list(map(int, str(p))) + list(map(int, str(m))) + list(map(int, str(m2)))
        digits = set(digits)
        if 0 in digits or len(digits) != 9:
            continue
        result_list.append(p)

print(sum(set(result_list)))