from math import sqrt

# By using herons formula and wolfram alpha i find that these two eqations solve the problem

def px(n):
	return 1/3*((7 - 4*sqrt(3))**n + (7 + 4*sqrt(3))**n + 1)

def mx(n):
	return 1/3*(2*(7 - 4*sqrt(3))**n + sqrt(3)*(7 - 4*sqrt(3))**n + 2*(7 + 4*sqrt(3))**n - sqrt(3)*(7 + 4*sqrt(3))**n - 1)

r = 0

n = 1

while 3*round(px(n)) - 1 < 10**9:
	r += 3*round(px(n)) - 1
	n += 1

n = 1

while 3*round(mx(n)) - 1 < 10**9:
	r += 3*round(mx(n)) + 1
	n += 1

print(r - 4)

