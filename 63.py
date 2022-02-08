"""
The 5-digit number, 16807=75, is also a fifth power. 
Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

result = 0

for n in range(1,30):
    for d in range(1,10):
        r = d**n
        if len(str(r)) == n:
            result += 1

print(result)
