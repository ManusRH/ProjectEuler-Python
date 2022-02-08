"""
Find the lowest sum for a set of five primes for which any two
 primes concatenate to produce another prime.
"""
from eulerlib import primes, is_prime

def concatenable(p, pl):
    result = []
    for c in pl:
        if c != p:
            if is_prime(int(str(p)+str(c))) and is_prime(int(str(c)+str(p))):
                result.append(c)
    return result

pl = primes(10000)[2:-1]

resultsall = []

for p1 in [7, 13]: # 5 will never work, already tried all of 3
    for p2 in pl:
        if p1 == p2: continue

        p1c = concatenable(p1, pl)
        p2c = concatenable(p2, pl)

        pin = [x for x in p1c if x in p2c]
        if not pin: continue

        result = [p1, p2]

        b = False

        for pp1 in pin:
            for pp2 in pin:
                for pp3 in pin:
                    if pp1 != pp2 and pp1 != pp3 and pp2 != pp3:
                        if is_prime(int(str(pp1)+str(pp2))) \
                        and is_prime(int(str(pp2)+str(pp1))) \
                        and is_prime(int(str(pp1)+str(pp3))) \
                        and is_prime(int(str(pp3)+str(pp1))) \
                        and is_prime(int(str(pp2)+str(pp3))) \
                        and is_prime(int(str(pp3)+str(pp2))):
                            result.append(pp1)
                            result.append(pp2)
                            result.append(pp3)
                            b = True
                if b: break
            if b: break

        if len(result) == 5:
            resultsall.append(sum(result))
            print(resultsall, "WOW")

print(min(resultsall))

# Very slow
