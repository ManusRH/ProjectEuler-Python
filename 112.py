"""
Working from left-to-right if no digit is exceeded by the digit
to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is
called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor
decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but
just over half of the numbers below one-thousand (525) are bouncy.
In fact, the least number for which the proportion of bouncy numbers
first reaches 50\% is 538.

Surprisingly, bouncy numbers become more and more common and by the
time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is 
exactly 99%.
"""
from fractions import Fraction

p = 1
n = 99
b = 0

while b/n < 0.99:
    l = [int(x) for x in list(str(n))]

    if all([l[x] <= l[x+1] for x in range(len(l)-1)]):
        pass
    elif all([l[x] >= l[x+1] for x in range(len(l)-1)]):
        pass
    else:
        b += 1
    n += 1

print(n-100) # because 0 .. 100 don't count ??? WHAT
