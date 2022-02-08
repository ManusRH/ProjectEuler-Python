from math import factorial

result = 0

for i in range(3, 1000000):
    j = str(i)
    r = 0
    for e in j:
        e = int(e)
        r += factorial(e)
    if i == r:
        print(i)
        result += i

print(result)