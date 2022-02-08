"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up
of each of the digits 0 to 9 in some order, but it also has a rather
interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we
note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""
from itertools import permutations

result = 0

perx = list(permutations([0,1,2,3,4,5,6,7,8,9]))

per = []

for e in perx:
    t = []
    for f in e:
        t.append(str(f))
    per.append(t)

for p in per:
    if int(p[1]+p[2]+p[3]) % 2 == 0 and int(p[2]+p[3]+p[4]) % 3 == 0:
        if int(p[3]+p[4]+p[5]) % 5 == 0 and int(p[4]+p[5]+p[6]) % 7 == 0:
             if int(p[5]+p[6]+p[7]) % 11 == 0 and int(p[6]+p[7]+p[8]) % 13 == 0:
                 if int(p[7]+p[8]+p[9]) % 17 == 0:
                     result += int(p[0]+p[1]+p[2]+p[3]+p[4]+p[5]+p[6]+p[7]+p[8]+p[9])
print(result)
#??? what's wrong?
