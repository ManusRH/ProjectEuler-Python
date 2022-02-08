import sympy
from math import factorial

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b//a, b%a
        m,n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

def modinv(a, m):
    g, x, y = egcd(a, m) 
    if g != 1:
        return None
    else:
        return x % m

def s(p):
    a = modinv(p-2, p)
    b = modinv(p-3, p)
    c = modinv(p-4, p)
    return (a + a*b + a*b*c) % p

primes = list(sympy.sieve.primerange(5, 10**8))

print("Primes are done")

print(sum(s(p) % p for p in primes))
