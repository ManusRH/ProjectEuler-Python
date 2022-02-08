"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six
of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this
5-digit number is the first example having seven primes among the ten
generated numbers, yielding the family: 56003, 56113, 56333, 56443,
56663, 56773, and 56993. Consequently 56003, being the first member of
this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an eight
prime value family.
"""
from eulerlib import primes, is_prime

def q(n, f):
    n = [x for x in list(str(n))]
    f = [x for x in list(str(f))]
    if len(f) > len(n): return "skip"
    while len(f) <= len(n):
        f.insert(0, "0")
    del f[0]
    for p in range(len(n)):
        if f[p] == "1":
            n[p] = "0"
    n = int("".join(n))
    return n

for l in range(7):
    lim = 10**l

    p = [x for x in primes(lim) if x > lim//10]
    fl = [x for x in range(lim) if all((str(x)[y] == "1" or str(x)[y] == "0") for y in range(len(str(x))))]

    for n in p:
        print(n)
        for f in fl:
            nn = q(n, f)
            if nn == "skip": continue
            np = 0
            for m in range(10):
                #print(n, f, nn + f*m)
                if is_prime(nn + f*m) and nn + f*m > lim//10:
                    np += 1
            if np == 8:
                print("FOUND:", n, f)
                exit()
# Do some calculations correct = 121313
