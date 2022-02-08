# -*- coding: utf-8 -*-
"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value
is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle words?
"""
def word_value(word):
    value = 0
    for l in word:
        if l == "A":
            value += 1
        elif l == "B":
            value += 2
        elif l == "C":
            value += 3
        elif l == "D":
            value += 4
        elif l == "E":
            value += 5
        elif l == "F":
            value += 6
        elif l == "G":
            value += 7
        elif l == "H":
            value += 8
        elif l == "I":
            value += 9
        elif l == "J":
            value += 10
        elif l == "K":
            value += 11
        elif l == "L":
            value += 12
        elif l == "M":
            value += 13
        elif l == "N":
            value += 14
        elif l == "O":
            value += 15
        elif l == "P":
            value += 16
        elif l == "Q":
            value += 17
        elif l == "R":
            value += 18
        elif l == "S":
            value += 19
        elif l == "T":
            value += 20
        elif l == "U":
            value += 21
        elif l == "V":
            value += 22
        elif l == "W":
            value += 23
        elif l == "X":
            value += 24
        elif l == "Y":
            value += 25
        elif l == "Z":
            value += 26
    return value

trianglenumbers = []

for i in range(1, 200):
    i = 0.5 * i*(i+1)
    trianglenumbers.append(i)

result = 0

with open('42_words.txt') as f:
    words = f.read().split('"')

for word in words:
    if word_value(word) in trianglenumbers:
        result += 1

print(result)
