"""
Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?
"""
import math

m = 50

r = []

for x1 in range(0,m+1):
    print(x1)
    for y1 in range(0,m+1):
        for x2 in range(0,m+1):
            for y2 in range(0,m+1):
                # and the last point is at (0,0)
                # P = (x1,y1), Q = (x2,y2), O = (0,0)

                #SIDES
                OP = math.sqrt(x1**2 + y1**2)
                OQ = math.sqrt(x2**2 + y2**2)
                PQ = math.sqrt((x1-x2)**2 + (y1-y2)**2)

                if OP == 0 or OQ == 0 or PQ == 0: continue

                # ANGLES
                angO = math.acos( round((OP**2 + OQ**2 - PQ**2)/(2*OP*OQ), 5) )*180/math.pi
                angP = math.acos( round((PQ**2 + OP**2 - OQ**2)/(2*PQ*OP), 5) )*180/math.pi
                angQ = math.acos( round((OQ**2 + PQ**2 - OP**2)/(2*OQ*PQ), 5) )*180/math.pi

                if round(angO, 5) == 90 \
                or round(angP, 5) == 90 \
                or round(angQ, 5) == 90:
                    if ((x1,y1),(x2,y2)) not in r and ((x2,y2),(x1,y1)) not in r:
                        r.append(((x1,y1),(x2,y2)))


print("Success!", len(r))
