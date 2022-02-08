# -*- coding: utf-8 -*-
"""
In England the currency is made up of pound, £, and pence, p,
and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
def count(p1, p2, p5, p10, p20, p50, p100):
    return p1*1 + p2*2 + p5*5 + p10*10 + p20*20 + p50*50 + p100*100

result = 1

for p1 in range(201):
    if count(p1,0,0,0,0,0,0) > 200:
        break
    elif count(p1,0,0,0,0,0,0) == 200:
        result += 1
        break

    for p2 in range(101):
        if count(p1,p2,0,0,0,0,0) > 200:
            break
        elif count(p1,p2,0,0,0,0,0) == 200:
            result += 1
            break

        for p5 in range(41):
            if count(p1,p2,p5,0,0,0,0) > 200:
                break
            elif count(p1,p2,p5,0,0,0,0) == 200:
                result += 1
                break

            for p10 in range(21):
                if count(p1,p2,p5,p10,0,0,0) > 200:
                    break
                elif count(p1,p2,p5,p10,0,0,0) == 200:
                    result += 1
                    break

                for p20 in range(11):
                    if count(p1,p2,p5,p10,p20,0,0) > 200:
                        break
                    elif count(p1,p2,p5,p10,p20,0,0) == 200:
                        result += 1
                        break

                    for p50 in range(5):
                        if count(p1,p2,p5,p10,p20,p50,0) > 200:
                            break
                        elif count(p1,p2,p5,p10,p20,p50,0) == 200:
                            result += 1
                            break

                        for p100 in range(3):
                            if count(p1,p2,p5,p10,p20,p50,p100) > 200:
                                break
                            elif count(p1,p2,p5,p10,p20,p50,p100) == 200:
                                result += 1
                                break
print(result)
