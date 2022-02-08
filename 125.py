"""
Find the sum of all the numbers less than 10^8 that are both
palindromic and can be written as the sum of consecutive squares.
"""
def is_palindromic(n):
    if all([str(n)[x] == str(n)[-(x+1)] for x in range(len(str(n))//2)]):
        return True
    else:
        return False

result = 0
mem = []

for e in range(1, 10001):
    print(e)
    for s in range(e-1, 0, -1):
        p = sum([x**2 for x in range(s, e+1)])
        if is_palindromic(p) and p < 100000000 and p not in mem:
            result += p
            mem.append(p)
        elif p > 100000000:
            break

print(result)
