"""
Starting with 1 and spiralling anticlockwise in the following way, 
a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right 
diagonal, but what is more interesting is that 8 out of the 13 numbers 
lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square 
spiral with side length 9 will be formed. If this process is continued, 
what is the side length of the square spiral for which the ratio of primes 
along both diagonals first falls below 10%?
"""
from eulerlib import is_prime
from math import floor

n = 2
wait = 2
t = 0

primes_d = 0
number_d = 0
percent = 1

f = True

while percent > 0.1 or f:
    if n % wait == 1:
        t += 1
        if is_prime(n):
            primes_d += 1
        number_d += 1


    if t % 4 == 0 and t != 0:
        t = 0
        wait += 2
        print(percent)

    if n > 49:
        f = False
        percent = primes_d/number_d

    n += 1


print(wait - 1)

