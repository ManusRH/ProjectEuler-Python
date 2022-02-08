"""
It is possible to write five as a sum in exactly 
six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written 
as a sum of at least two positive integers?
"""
p = range(1, 100)
result = [1] + [0]*100
print(result)
for n in p:
    for i in range(n, 101):
        result[i] += result[i-n]

print(result[100])
