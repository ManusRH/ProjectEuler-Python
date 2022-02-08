"""
In the following equation x, y, and n are positive integers.

1/x + 1/y = 1/n

What is the least value of n for which the number of distinct solutions exceeds one-thousand?
"""

n = 180000 #Checked up till here

while True:
    n += 10 #It appeared 10's had the most solutions

    y_solutions = 0

    x = n
    
    while x < 2*n:
        x += 1

        if (n*x) % (n-x) == 0:
            y_solutions += 1

    print("n:", n, "s:", y_solutions)

    if y_solutions > 1000:
        print(n)
        break

