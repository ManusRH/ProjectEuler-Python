"""
Find the least value of n for which p(n) is divisible by one million.
"""
# Using https://en.wikipedia.org/wiki/Pentagonal_number_theorem


def g(k):
	return k*(3*k - 1)//2

ps = [1,1]

n = 2

while True:
	p = 0
	k = 1
	while n - g(k) + 1 > 0:
		p += (int((-1)**(k-1)) % 1000000)*ps[n-g(k)] % 1000000
		if k > 0:
			k *= -1
		else:
			k *= -1
			k += 1
	ps.append(p)
	print(n, " : ", p)
	if p % 1000000 == 0:
		break
	n += 1

# 55374
