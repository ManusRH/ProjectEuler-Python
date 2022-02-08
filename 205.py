"""
Peter has nine four-sided (pyramidal) dice, 
each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each 
with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare 
totals: the highest total wins. The result 
is a draw if the totals are equal.

What is the probability that Pyramidal Pete 
beats Cubic Colin? Give your answer rounded 
to seven decimal places in the form 0.abcdefg
"""

from random import randint
# Laver en simulation

p_win = 0
total = 50000000

for s in range(total):
	peter = sum([randint(1,4) for x in range(1,10)])
	colin = sum([randint(1,6) for x in range(1,7)])
	if peter > colin:
		p_win += 1

print(p_win/total)
print(p_win)
"""

p_rolls = [0, 0,  0,  1,   9,  45, 165, 486, 1206, 2598, 4950, 8451, 13051, 18351, 23607,27876, 30276, 30276, 27876, 23607, 18351, 13051, 8451, 4950, 2598, 1206, 486, 165, 45, 9, 1]

c_rolls = [1, 6, 21, 56, 126, 252, 456, 756, 1161, 1666, 2247, 2856, 3431, 3906, 4221,4332, 4221, 3906, 3431, 2856, 2247, 1666, 1161, 756, 456, 252, 126, 56, 21, 6, 1]
 
p_win = 0
total = (4**9) * (6**6.)
for colin in range(0, 31):
    for peter in range (colin+1, 31):
        p_win += p_rolls[peter]*c_rolls[colin]
 
print(p_win/total)

"""
