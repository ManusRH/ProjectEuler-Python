"""
Find the sum of FITs for the BOPs.
"""
import numpy as np

def OP(p, Y): #p number of points
    m = np.matrix([[x] for x in Y[:p]])

    t = []

    for a in range(1,p+1):
        tt = []
        for b in range(0,p):
            tt.append(a**b)
        t.append(sorted(tt)[::-1])

    t = np.matrix(t).getI()
    r = np.matmul(t, m)
    c = np.squeeze(np.asarray(r))

    result = 0

    if p != 1:
        e = len(c)-1
        for h in c:
            result += h*(p+1)**e
            e -= 1
    elif p == 1:
        result = 1

    return result

poly = lambda n: 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

# We need 11 points
X = [range(1, 12)]
Y = [poly(x) for x in range(1, 12)]

final = 0

for n in range(1,11):
    final += OP(n, Y)

print(final) # without the .6

# Algorithm used: http://mth.bz/fit/polyfit/findcurv.htm
