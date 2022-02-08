"""
Find the sum of the only ordered set of six cyclic 4-digit numbers for which
each polygonal type: triangle, square,pentagonal, hexagonal, heptagonal,
and octagonal, is represented by a different number in the set.
"""
from math import sqrt
from itertools import permutations

p3 = lambda n: n*(n+1)/2
p4 = lambda n: n**2
p5 = lambda n: n*(3*n-1)/2
p6 = lambda n: n*(2*n-1)
p7 = lambda n: n*(5*n-3)/2
p8 = lambda n: n*(3*n-2)

p3l = [int(p3(x)) for x in range(1,10000) if 1000 <= p3(x) <= 9999]
p4l = [int(p4(x)) for x in range(1,10000) if 1000 <= p4(x) <= 9999]
p5l = [int(p5(x)) for x in range(1,10000) if 1000 <= p5(x) <= 9999]
p6l = [int(p6(x)) for x in range(1,10000) if 1000 <= p6(x) <= 9999]
p7l = [int(p7(x)) for x in range(1,10000) if 1000 <= p7(x) <= 9999]
p8l = [int(p8(x)) for x in range(1,10000) if 1000 <= p8(x) <= 9999]

reeee = []
pall = [p3l, p4l, p5l, p6l, p7l, p8l]

for pstart in pall:
    for pstarti in pstart:
        pallp = list(permutations(pall))

        for palln in pallp:
            result = []
            find = str(pstarti)[-2] + str(pstarti)[-1] #
            for pnl in palln:
                for ipn in pnl:
                    if str(ipn)[0] + str(ipn)[1] == find: #
                        result.append(ipn)
                        find = str(ipn)[-2] + str(ipn)[-1] #

            if sorted(result) not in reeee:
                if len(result) == 6:
                    if str(result[0])[0] + str(result[0])[1] == str(result[-1])[-2] + str(result[-1])[-1]:
                        print(result)
                        print("WOW", sum(result))
                        print()

            reeee.append(sorted(result))

# Gives 5 answers; 2nd one was correct.
