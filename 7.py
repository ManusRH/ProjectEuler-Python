"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

is_prime = [True for i in range(1000000)]
primes   = []

p = 2

while 1:
    if is_prime[p]:
        print(p)
        primes.append(p)
        for i in range(p*2, 1000000, p):
            is_prime[i] = False
    if len(primes) == 10001:
        break
    p += 1

print()
print(primes[-1])
