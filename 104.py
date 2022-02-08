"""
Given that Fk is the first Fibonacci number for which the first nine digits AND
the last nine digits are 1-9 pandigital, find k.
"""

def next_fib(p1, p2, k):
    return p1+p2, k+1

found = False

fm1 = 1
f = 1
k = 2

while not found:
    t = f
    f, k = next_fib(fm1, f, k)
    fm1 = t

    first = set(str(f)[:9])
    last  = set(str(f*10 % 10000000000))
    find  = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    if len(first) == 9 and len(last) == 10 and "0" not in first:
        print("FOUND:", k)
        found = True
        print(f)
    else:
        print(k)

# Only takes 8929 seconds
