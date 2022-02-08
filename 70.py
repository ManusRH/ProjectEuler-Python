"""
Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of
n and the ratio n/φ(n) produces a minimum.
"""
from sympy import sieve

def is_perm(n, m):
	if sorted(str(n)) == sorted(str(m)):
		return True
	else:
		return False

primes = list(sieve.primerange(1, 10000))

best = 10000

for i in range(1, len(primes)):
	#print(i)
	for j in range(1, len(primes)):
		n = primes[i]*primes[j]
		phi = (primes[i]-1) * (primes[j]-1)

		r = n/phi

		if n > 10**7: break

		if is_perm(n, phi) and r < best:
			best = r
			print(n, r)








