import random
from optparse import OptionParser

maxrounds = 5_000_000
round = 0
current = 0
numfields = 40
count = [0]*numfields
pasch = 0

GO = 0
CC1 = 2
R1 = 5
CH1 = 7
JAIL = 10
C1 = 11
U1 = 12
R2 = 15
CC2 = 17
FP = 20
CH2 = 22
E3 = 24
R3 = 25
U2 = 28
G2J = 30
CC3 = 33
R4 = 35
CH3 = 36
H2 = 39


def check_state(n):
    global count
    result = ""
    result2 = ""
    first3 = ""
    for i in range(numfields):
        result += str(count[i]) + " "
    print("result after", n, "iterations:", result)
    
    sortedcount = count.copy()
    sortedcount.sort(reverse=True)
    firstn = 0
    prev_value = -1
    for value in sortedcount:
        if firstn >= 5: break
        if value == prev_value: continue
        #print("value:", value)
        for index in range(numfields):
            if firstn >= 5: break
            if count[index] == value:
                firstn += 1
                print(index, ":", count[index])
                first3 += "%2.2d" % index
                prev_value = value
    print("result:", first3[:6])

d3 = random.randint(0, 15)
d4 = random.randint(0, 15)

for i in range(maxrounds):
    round += 1
    d1 = random.randint(1, 4)
    d2 = random.randint(1, 4)
    
    if d1 == d2:
        pasch += 1
    else:
        pasch = 0
        
    if pasch >= 3:
        current = JAIL
        pasch = 0
    else:       
        current = (current + d1 + d2) % numfields
    
    if current == G2J:
        current = JAIL
    elif (current == CC1 or current == CC2 or current == CC3):       
        if d3 == 0: current = GO
        elif d3 == 1: current = JAIL
        else: pass
        d3 = (d3 + 1) % 16
    elif (current == CH1 or current == CH2 or current == CH3):
        if d4 == 0 or d4 > 10: pass
        elif d4 == 1: current = GO
        elif d4 == 2: current = JAIL
        elif d4 == 3: current = C1 
        elif d4 == 4: current = E3
        elif d4 == 5: current = H2
        elif d4 == 6: current = R1
        elif d4 == 7 or d4 == 8: 
            if current > R1 and current < R2: current = R2
            elif current > R2 and current < R3: current = R3
            elif current > R3 and current < R4: current = R4
            else: current = R1
        elif d4 == 9:
            if current > U1 and current < U2: current = U2
            else: current = U1
        elif d4 == 10:
            current = (current + numfields - 3) % numfields
            if current == CC3:
                if d3 == 3: current = GO
                elif d3 == 12: current = JAIL
                else: pass
                d3 = (d3 + 1) % 16
        else:
            print("impossible dice d4:", d4)
            exit(0)
        d4 = (d4 + 1) % 16         
    
    count[current] += 1
    if round == maxrounds: break
   

check_state(round)