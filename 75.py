from math import sqrt, floor

m = 0
lim = 1500000
l = (lim + 1)*[[]]
l = [[] for x in range(lim+1)]

while m < sqrt(lim):
    m += 1
    for n in range(1, m):
        k = 1
        while 2*m*(m+n)*k <= lim:
            if sorted([k*(m**2 - n**2), k*2*m*n, k*(m**2 + n**2)]) not in l[2*m*(m+n)*k]:
                l[2*m*(m+n)*k].append(sorted([k*(m**2 - n**2), k*2*m*n, k*(m**2 + n**2)]))
            k += 1
    
    print(m, sqrt(lim))

llen = list(map(len, l))

print(llen.count(1))
