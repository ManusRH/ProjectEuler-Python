"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
with open('p022_names.txt') as f:
    names = f.read().split('"')
    names.sort()

t = []

for i in names:
    if i != ',' and i != '':
        t.append(i)

result = 0

def score(name):
    sc = 0
    for i in name:
        if i == "A": sc += 1
        elif i == "B": sc += 2
        elif i == "C": sc += 3
        elif i == "D": sc += 4
        elif i == "E": sc += 5
        elif i == "F": sc += 6
        elif i == "G": sc += 7
        elif i == "H": sc += 8
        elif i == "I": sc += 9
        elif i == "J": sc += 10
        elif i == "K": sc += 11
        elif i == "L": sc += 12
        elif i == "M": sc += 13
        elif i == "N": sc += 14
        elif i == "O": sc += 15
        elif i == "P": sc += 16
        elif i == "Q": sc += 17
        elif i == "R": sc += 18
        elif i == "S": sc += 19
        elif i == "T": sc += 20
        elif i == "U": sc += 21
        elif i == "V": sc += 22
        elif i == "W": sc += 23
        elif i == "X": sc += 24
        elif i == "Y": sc += 25
        elif i == "Z": sc += 26
    return sc

multi = 1

for i in t:
    s = score(i)
    result += s * multi
    multi += 1

print(result)

