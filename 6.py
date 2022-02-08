"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

sum_list_square = []

for i in range(0,101):
	sum_list_square.append(i**2)

each = (sum(sum_list_square))

sum_list = []

for j in range(0,101):
	sum_list.append(j)

summed = sum(sum_list)**2

print(summed - each)
