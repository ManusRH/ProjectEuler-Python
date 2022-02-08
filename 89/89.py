"""
For a number written in Roman numerals to be considered valid there 
are basic rules which must be followed. Even though the rules allow 
some numbers to be expressed in more than one way there is always a 
"best" way of writing a particular number.

For example, it would appear that there are at least six ways of 
writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, 
and the last example is considered to be the most efficient, as 
it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target 
As...'), contains one thousand numbers written in valid, but not 
necessarily minimal, Roman numerals; see About... Roman Numerals 
for the definitive rules for this problem.

Find the number of characters saved by writing each of these in 
their minimal form.

Note: You can assume that all the Roman numerals in the file 
contain no more than four consecutive identical units.
"""
from math import floor

def make_roman(n):
    num_rom = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
               (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    result = ''
    while n > 0:
        for num, rom in num_rom:
            while n >= num:
                result += rom
                n -= num
    return result

def make_decimal(r):
    result = 0
    li = 0
    r = list(r)
    print(r)

    while li != len(r):
        if r[li] != r[-1]:
            if r[li] + r[li+1] == 'CM':
                result += 900
                li += 2
                continue
            elif r[li] + r[li+1] == 'CD':
                result += 400
                li += 2
                continue
            elif r[li] + r[li+1] == 'XC':
                result += 90
                li += 2
                continue
            elif r[li] + r[li+1] == 'XL':
                result += 40
                li += 2
                continue
            elif r[li] + r[li+1] == 'IX':
                result += 9
                li += 2
                continue
            elif r[li] + r[li+1] == 'IV':
                result += 4
                li += 2
                continue
        if r[li] == "M":
            result += 1000
            li += 1
        elif r[li] == "D":
            result += 500
            li += 1
        elif r[li] == "C":
            result += 100
            li += 1
        elif r[li] == "L":
            result += 50
            li += 1
        elif r[li] == "X":
            result += 10
            li += 1
        elif r[li] == "V":
            result += 5
            li += 1
        elif r[li] == "I":
            result += 1
            li += 1
    return result

numbers = []

with open("roman.txt", "r") as f:
    for line in f:
        line = line.strip('\n')
        numbers.append(line)

result = 0

for n in numbers:
    result += len(n) - len(make_roman(make_decimal(n)))

print(result)

# Make make_roman() include subtractive rules
# https://projecteuler.net/about=roman_numerals