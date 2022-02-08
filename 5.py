"""
2520 is the smallest number that can be divided by each of the
numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by
all of the numbers from 1 to 20?
"""
num = []
for i in range(0,100000000000,20):
	temp = []
	for j in range(1,21):
		if i % j == 0:
			temp.append(True)
		else:
			temp.append(False)
	if all(temp) and i != 0:
		num.append(i)
		break
print(num)
