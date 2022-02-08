"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

result = 0

for i in range(1, 10000001):
    while True:
        i = list(str(i))
        digits = []
        for e in i:
            digits.append(int(e)**2)
        i = sum(digits)
        if i == 1:
            break
        if i == 89:
            result += 1
            break
    print(result)

print()
print(result)
