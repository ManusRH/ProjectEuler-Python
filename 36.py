"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

temp_pal = [1, 2, 3, 4, 5, 6, 7, 8, 9]

pal = []
pal_2 = []

# Make palindromes
# All even length palindromes
for i in range(1, 1000):  # 1 to 999 (+) 999 = 999999 < 1000000
    p = str(i) + str(i)[::-1]
    temp_pal.append(int(p))

# The rest of the palindromes
for i in temp_pal:
    if 9 < i < 100000:  # if 1 digit added to 100000 the i > 1000000
        for e in range(10):
            p = list(str(i))
            q = int(len(str(i)) / 2)
            p.insert(q, str(e))
            p = int("".join(p))
            if p not in temp_pal:
                pal.append(p)

# Merge the lists
for i in temp_pal:
    if i not in pal:
        pal.append(i)

# Find out if the binary version is palindrome as well
for i in sorted(pal):
    b = "{0:b}".format(i)
    for e in range(len(b)):
        if b[e] != b[-(e + 1)]:
            break
        elif e == len(b) - 1:
            pal_2.append(i)

print(sum(pal_2))
