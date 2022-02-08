"""
How many reversible numbers are there below one-billion
"""

ns = [x for x in range(9, 10**9 ,2) if int(str(x)[0]) % 2 == 0]

result = 0

for n in ns:
    if all([int(x) % 2 == 1 for x in list(str(int(str(n)[::-1]) + n))]):
        result += 1

print(result*2)

# ra = ns * 2

# Very slow - around 1000 seconds
