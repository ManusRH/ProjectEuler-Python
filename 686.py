from math import log10, floor

# log10(2) ~ 0.301029995663981195213738894724493026768189881462108541310...

d = 2

def p(L, n):
    k = 0
    j = 1
    f = j*0.301029995663981195213738894724493 - floor(j*0.301029995663981195213738894724493)
    p = 10**(f+d)
    while p != L or k != n:
        j += 1
        f = j*0.301029995663981195213738894724493 - floor(j*0.301029995663981195213738894724493)
        p = floor(10**(f+d))
        #print(j, 2**j, p, (10**(int(j*0.301029995663981195213738894724493)-d)), k)
        if p == L:
            k += 1
        #print(j,k)
    return j

print(p(123,678910))

# super slow but it works (190 seconds)
