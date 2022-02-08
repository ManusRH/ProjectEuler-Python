"""
Using up to one million tiles how many different square laminae can be formed?
"""

k = 1
n = k + 2
r = 0

while True:
    if ((n**2) - (k**2)) <= 10**6:
        r += 1
    else:
        k += 1
        n = k
        #print(k, r)

    n += 2

    if k >= 250000:
        print("RESULT!", r)
        break

