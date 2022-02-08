"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

# 1-9
onenine = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4 #36

# 10-19
tennineteen = 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8 #70

# 20-99
twentynintynine = 10 * (6 + 6 + 5 + 5 + 5 + 7 + 6 + 6) + 8 * onenine #748

# 1-100
oneonehundred = onenine + tennineteen + twentynintynine

#
hundredtimes = 36 * 100
ninetimes = 9 * oneonehundred
hundredninetimes = 7 * 9
hundredand = 9 * 99 * 10
onethousend = 11

print(21124)
