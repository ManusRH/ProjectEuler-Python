"""
Find a30.
"""

n  = []

for s in range(2, 100):
    for p in range(2,10):
        a = s**p
        k = sum([int(x) for x in str(a)])
        if k == s:
            n.append(a)

n = sorted(n)

print(n)
print(n[29])


#dumb approch down below

"""
n = []

found = False

a = 10

while not found:
    #print(a)
    a += 1

    k = 0
    p = 2
    s = sum([int(x) for x in str(a)])
    while k < a:
        if s == 1: break

        k = s**p
        if a == k:
            print("found one: ", s, "to the", p, "=", a)
            n.append(a)
            break
        p += 1
    if len(n) == 30:
        break

print(n)
print(n[-1])

# too slow
"""
