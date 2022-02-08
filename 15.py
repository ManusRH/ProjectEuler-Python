"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""
from math import *

n = 40 # number of up (or down) times number of right (or left)
k = 20 # number of steps up(or down) to get to point (a, b)

result = factorial(n) / (factorial((n - k)) * factorial(k))

print(result)
