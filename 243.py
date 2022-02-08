"""
Find the smallest denominator d, having a resilience R(d) < 15499/94744 .
"""

def phi(n): # Eulers phi function. Easy to see that R(d) = phi(d)/(d-1).
     
    result = n
    p = 2
    while(p * p <= n):
        if (n % p == 0):
            while (n % p == 0):
                n = int(n / p)

            result -= int(result / p)

        p += 1

    if (n > 1):
        result -= int(result / n)
    return result

def SieveOfEratosthenes(n): # Actually gives us the products of the first k primes which are less than n.
    prime = [True for i in range(n + 1)]
    p = 2

    l = [2]

    while (p * p <= n):
        if (prime[p] == True):
            l.append(p * l[-1])
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1

    return(l)


ld, lr = 94744, 15499 #The limits from the problem.

q = SieveOfEratosthenes(841) #We find that the result is somewhere between 446185740 and 12939386460

q2 = []
for i in q: # Here we multiply up the products of primes we found (idk why; maybe because it's intuitive)
    if i == 2 or i == 4 or i == 12 or i == 420 or i == 60: continue #Because fuck these numbers they take too long to multiply up.
    k = 1
    while k*i <= 12939386460: #because we *know* n = 12939386460 solves the problem
        q2.append(k*i)
        k += 1

n = 2

while ld * phi(q2[n]) >= lr * (q2[n]-1): # I.e. ld/lr >= phi(q2[n])/(q2[n]-1)
    n += 1

print("Result found: ", q2[n])

# Takes about 6 seconds to run.


"""
def R(d):
    rn = 0
    rd = d-1
    if d % 2 == 0:
        for numer in range(1, d, 2):
            if GCD(numer, d) == 1:
                rn += 1
    else:
        for numer in range(1, d):
            if GCD(numer, d) == 1:
                rn += 1
    return rn, rd

print("k")

ln = 15499
ld = 94744

d = 2

while 1:
    rn, rd = R(d)
    if (rn * ld) < (ln * rd):
        print("FOUND:", d)
        break
    if d % 1000 == 0:
        print(d)
    d += 1
"""