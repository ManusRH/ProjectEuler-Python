"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""
"""
all_numbers = [1]

primes = [1]

while primes[-1] < 2000000:
	for i in all_numbers:
		temp = []
		all_numbers.append(all_numbers[-1]+1)
		for j in range(2,i-1,2):
			temp.append(i % j)
		if 0 not in temp:
			primes.append(i)
			print(primes[-1])
		if primes[-1] > 2000000:
			break

del primes[-1]
del primes[0]
print(primes)
print()
print(sum(primes))
"""

# IKKE MIT
import math, sys

def prime_sieve(limit):
    # Mark everything prime to start
    primes = [1 for x in range(limit)]
    primes[0] = 0
    primes[1] = 0

    # Only need to sieve up to sqrt(limit)
    imax = int(math.sqrt(limit) + 1)

    i = 2
    while (i < imax):
        j = i + i
        while j < limit:
            primes[j] = 0
            j += i

        # Move i to next prime
        while True:
           i += 1
           if primes[i] == 1:
               break

    return primes

s = prime_sieve(2000000)
print(sum(i for i in range(len(s)) if s[i] == 1))
