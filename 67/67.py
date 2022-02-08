"""
By starting at the top of the triangle below and moving to adjacent 
numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt 
(right click and 'Save Link/Target As...'), a 15K text file 
containing a triangle with one-hundred rows.
"""

triangle = []

with open('p067_triangle.txt', 'r') as f:
    for line in f:
        line = line.strip('\n')
        rowski = [int(x) for x in line.split(" ")]
        triangle.append(rowski)

skip = True
rowbefore = []
for row in reversed(triangle):
    if skip:
        rowbefore = row
        skip = False
        continue

    new_row = []

    for i in range(0,len(row)):
        if row[i]+rowbefore[i] > row[i]+rowbefore[i+1]:
            new_row.append(row[i]+rowbefore[i])
        else:
            new_row.append(row[i]+rowbefore[i+1])

    rowbefore = new_row

print(rowbefore)
