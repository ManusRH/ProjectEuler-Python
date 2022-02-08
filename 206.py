"""
Find the unique positive integer whose square has the
form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""
from eulerlib import is_square
from math import sqrt, floor

low  = 1020304050607080900 # 31942198
      #1_2_3_4_5_6_7_8_9_0
high = 1929394959697989900 # 439248785

for s in range(floor(sqrt(low)), floor(sqrt(high))+1, 2):
    ss = str(s*s)[::2]
    if ss == "1234567890":
        print(s)
        break

#VEEEEEEEEEEEEEEEEEERY SLOW
