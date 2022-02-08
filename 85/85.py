"""
Although there exists no rectangular grid that contains exactly two million 
rectangles, find the area of the grid with the nearest solution.
"""
def rec_count(k, n):
    if n == 0: return 0
    return rec_count(k, n-1) + n*((k**2+k)//2)

result = []


for a in range(1,100):
    for b in range(1,a+1):
        area = a*b
        r = rec_count(b, a)
        result.append((abs(r-2000000),area))

print(min(result))
