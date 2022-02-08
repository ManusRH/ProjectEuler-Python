"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

a = 600851475143
b = 2

while a != b:
	if a % b == 0:
		a //= b
	else:
		b += 1

print(b)
