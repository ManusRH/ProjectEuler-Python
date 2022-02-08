def s(n):
    return ((n % 9) + 1)*pow(10, n//9, 1000000007) - 1

def S(n):
    r = 6*(pow(10, n//9, 1000000007)-1) - 9*(n//9) % 1000000007

    for i in range(0, n%9):
        r += s(n-i) 

    return r % 1000000007

fib = [0,1]
r = 1
while len(fib) <= 90:
    fib.append(fib[r] + fib[r-1])
    r += 1

print(sum(S(f) for f in fib[2:]) % 1000000007)

