f = 0

for e in range(1,1001):
	f += e**e

f = str(f)
lastten = []
print(f)

for i in range(1,11):
	lastten.append(f[-i])

f = list(reversed(lastten))

print("".join(f))
