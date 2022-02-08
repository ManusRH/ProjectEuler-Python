"""
For 3 ≤ a ≤ 1000, find ∑ rmax.
"""
def rmax(a):
    result = 0
    for n in range(1,2000):
        r = ((a-1)**n + (a+1)**n) % (a**2)
        if r > result:
            result = r
    return result

r = 0

for a in range(3,1001):
    r += rmax(a)
    print(a)

print(r)

# I don't know what the algorithm was supposed to be but this bruteforce works
# ie i don't know how to be sure it's *the* maximum
