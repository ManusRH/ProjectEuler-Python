"""
How many hands does Player 1 win?
"""
def strip_dup(hand):
    r = []
    m = []
    r1 = []
    m1 = []
    for c in hand:
        if c[0] in r:
            m.append(c[0])
            m1.append(c)
            continue
        r.append(c[0])
        r1.append(c)
    t = list(set(r1) - set(m1))
    return t

def same_suit(hand):
    r = []
    for c in hand:
        r.append(c[1])
    if len(set(r)) == 1:
        return True
    return False

def royal_flush(hand):
    if not same_suit(hand):
        return 0
    r = []
    for c in hand:
        r.append(c[0])
    if "T" in r and "J" in r and "Q" in r and "K" in r and "A" in r:
        return 1000000000000000000
    return 0

def straight_flush(hand):
    if not same_suit(hand):
        return 0
    r = []
    for c in hand:
        if c[0] == "T":
            r.append(10)
            continue
        try:
            r.append(int(c[0]))
        except:
            return 0
    r = sorted(r)
    r[0] += 4
    r[1] += 3
    r[2] += 2
    r[3] += 1
    if len(set(r)) == 1:
        return 10000000000000000
    return 0

def four_of_kind(hand):
    r = []
    for c in hand:
        r.append(c[0])
    if len(set(r)) == 2:
        return 100000000000000
    return 0

def full_house(hand):
    r = []
    for c in hand:
        r.append(c[0])
    r = sorted(r)
    if r[0] == r[1] and r[2] == r[3] == r[4]:
        return 1000000000000
    elif r[0] == r[1] == r[2] and r[3] == r[4]:
        return 1000000000000
    return 0

def flush(hand):
    if same_suit(hand):
        return 10000000000
    return 0

def straight(hand):
    r = []
    for c in hand:
        if c[0] == "T":
            r.append(10)
            continue
        elif c[0] == "J":
            r.append(11)
            continue
        elif c[0] == "Q":
            r.append(12)
            continue
        elif c[0] == "K":
            r.append(13)
            continue
        elif c[0] == "A":
            r.append(14)
        try:
            r.append(int(c[0]))
        except:
            return 0
    r = sorted(r)
    if r[0] == r[1]-1 == r[2]-2 == r[3]-3 == r[4]-4:
        return 100000000 * r[0]
    return 0

def three_of_kind(hand):
    r = []
    for c in hand:
        r.append(c[0])
    if not len(set(r)) == 3:
        return 0
    r = sorted(r)
    for e in range(0,3):
        if r[e] == r[e+1] == r[e+2]:
            if r[e] == "T":
                m = 10
            elif r[e] == "J":
                m = 11
            elif r[e] == "Q":
                m = 12
            elif r[e] == "K":
                m = 13
            elif r[e] == "A":
                m = 14
            else:
                m = int(r[e])
    return 1000000

def two_pair(hand):
    r = []
    for c in hand:
        r.append(c[0])
    if not len(set(r)) == 3:
        return 0 
    r = sorted(r)
    for e in range(0,4):
        if r[e] == r[e+1]:
            if r[e] == "T":
                m = 10
            elif r[e] == "J":
                m = 11
            elif r[e] == "Q":
                m = 12
            elif r[e] == "K":
                m = 13
            elif r[e] == "A":
                m = 14
            else:
                m = int(r[e])
    return 10000 * m

def one_pair(hand):
    r = []
    m = 0
    for c in hand:
        r.append(c[0])
    if not len(set(r)) == 4:
        return 0
    r = sorted(r)
    for e in range(0,4):
        if r[e] == r[e+1]:
            if r[e] == "T":
                m = 10
            elif r[e] == "J":
                m = 11
            elif r[e] == "Q":
                m = 12
            elif r[e] == "K":
                m = 13
            elif r[e] == "A":
                m = 14
            else:
                m = int(r[e])
    return 100 * m 

def high_card(hand):
    r = []
    for c in hand:
        if c[0] == "T":
            r.append(10)
            continue
        elif c[0] == "J":
            r.append(11)
            continue
        elif c[0] == "Q":
            r.append(12)
            continue
        elif c[0] == "K":
            r.append(13)
            continue
        elif c[0] == "A":
            r.append(14)
        try:
            r.append(int(c[0]))
        except:
            return 0
    return max(r)

def who_win(hand1, hand2):
    hand1_result = 0
    hand2_result = 0

    #hand1_result += high_card(hand1)
    #hand2_result += high_card(hand2)

    if royal_flush(hand1):
        hand1_result += royal_flush(hand1)
    elif straight_flush(hand1):
        hand1_result += straight_flush(hand1)
    elif four_of_kind(hand1):
        hand1_result += four_of_kind(hand1)
    elif full_house(hand1):
        hand1_result += full_house(hand1)
    elif flush(hand1):
        hand1_result += flush(hand1)
    elif straight(hand1):
        hand1_result += straight(hand1)
    elif three_of_kind(hand1):
        hand1_result += three_of_kind(hand1)
    elif two_pair(hand1):
        hand1_result += two_pair(hand1)
    elif one_pair(hand1):
        hand1_result += one_pair(hand1)

    if royal_flush(hand2):
        hand2_result += royal_flush(hand2)
    elif straight_flush(hand2):
        hand2_result += straight_flush(hand2)
    elif four_of_kind(hand2):
        hand2_result += four_of_kind(hand2)
    elif full_house(hand2):
        hand2_result += full_house(hand2)
    elif flush(hand2):
        hand2_result += flush(hand2)
    elif straight(hand2):
        hand2_result += straight(hand2)
    elif three_of_kind(hand2):
        hand2_result += three_of_kind(hand2)
    elif two_pair(hand2):
        hand2_result += two_pair(hand2)
    elif one_pair(hand2):
        hand2_result += one_pair(hand2)

    if hand1_result > hand2_result:
        return True
    elif hand1_result == hand2_result:
        hand1_result += high_card(strip_dup(hand1))
        hand2_result += high_card(strip_dup(hand2))
        if hand1_result > hand2_result:
            return True
    return False

result = 0

with open('poker.txt', 'r') as f:
    for l in f:
        l = l.strip('\n').split(" ")
        hand1 = l[:5]
        hand2 = l[5:]
        print(hand2)
        if who_win(hand1, hand2):
            result += 1

print(result)

# What a tedious and fucking dumb problem
# The real answer is 376
