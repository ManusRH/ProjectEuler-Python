"""
How many chains, with a starting number below one million, 
contain exactly sixty non-repeating terms?
"""
def fac(n):
    if n == 1 or n == 0: return 1
    return fac(n-1)*n

def chain_next(n):
    return sum([fac(int(x)) for x in list(str(n))])

result = 0

for n in range(1000000):
    seen  = []
    now   = n
    while now not in seen:
        seen.append(now)
        now = chain_next(now)
        if len(seen) > 60: break
    if len(seen) == 60:
        result += 1
        print(n, result)

print(result)

# Slow but get the job done