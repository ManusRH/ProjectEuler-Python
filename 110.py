
# 1/x + 1/y = 1/n can be written as (x-n)(y-n) = n^2
# Therefore we need to find the smallest number n such that
# n^2 has more than 8,000,000 divisors.

# Stolen code to calculate this

from functools import reduce
 
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
 
mult = lambda x: reduce(lambda y, z: y * z, x, 1)
 
translate = lambda x: mult(primes[i] ** ((x[i] - 1) // 2) for i in range(len(x)))
 
def generator(limit):
    l = [1] * 14
    while l[13] < limit:
        i = 13
        while i > 0 and (l[i] == l[i-1]):
            l[i] = 1
            i -= 1
        l[i] += 2
        yield l
 
result = min(translate(l) for l in generator(13) if mult(l) > 8000000)
print(result)

