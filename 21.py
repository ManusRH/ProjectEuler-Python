"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
###

amicable = [0]


def find_devisors(n):
    temp = []
    for i in range(1, n):
        if n % i == 0:
            temp.append(i)
    return temp


def is_amicable(m):

    k = sum(find_devisors(m))

    if sum(find_devisors(k)) == m and k != m:
        amicable.append(m)

r = 1

while amicable[-1] < 10000:
    is_amicable(r)
    r += 1

amicable_safe = []

for i in amicable:
    if i < 10000:
        amicable_safe.append(i)

print(amicable_safe)
print(sum(amicable_safe))
