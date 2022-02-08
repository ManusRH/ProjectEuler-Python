"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

digits = 3

i = 10**digits - 1
j = i

while 1:
    print(i, j, i+j)
    n = i * j
    if all(str(n)[x] == str(n)[-(x+1)] for x in range(len(str(n))//2)):
        print(n)
        break

    if i == j:
        i -= 1
        j = 10**digits
    j -= 1


10+10=20
 9+10=19
 9+9 =18
 8+10=18
 8+9 =17
 8+8 =16
 7+10=17
 7+9 =16
 7+8 =15
 7+7 =14
 6+10=16
 6+9 =15

# DOESN'T WORK ATM. I wanted to make the higest sum of two number and then go
# down until it found one and then break
