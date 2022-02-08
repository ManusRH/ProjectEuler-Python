"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in 
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is 
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less 
than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, 
find the value of the denominator.
"""
l = []

for n in range(10,100):
    for d in range(10,100):
        if (n % 10 == 0 and d % 10 == 0) or n == d:
            continue
        t1 = [i for i in list(map(int, str(n))) if i in list(map(int, str(d)))]
        if len(t1) == 0:
            continue

        t2 = list(set(list(map(int, str(n))) + list(map(int, str(d)))))
        
        for i in t1:
            if i in t2:
                del t2[t2.index(i)]

        print(t2, n, d)
        if 0 not in t2 and len(t2) == 2:
            if t2[0]/t2[1] == n/d and t2[0] < t2[1]:
                l.append([n,d])

print(l) # 23/32 is wrong, the remaining one is 48/98
#then just add those 4 fractions up: answer is 1/100 --> 100
