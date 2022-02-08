from math import log

exps = []
biggest = 0

with open("99.txt", "r") as f:
    for l in f:
        l = l.strip("\n").split(",")
        a = int(l[0])
        x = int(l[1])
        b = x * log(a)
        exps.append(b)
        if biggest < b:
            biggest = b

print(exps.index(biggest) + 1)
