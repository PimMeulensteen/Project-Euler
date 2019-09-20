#Solved!
#55
import math

def isP(n):
    n = int(n)
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(n**0.5) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

primes = [2]
for x in range(3,1000000,2):
    y = str(x)
    lis = [y]

    for i in range(0,len(y)-1):
        lis.append(int(y[-1] + y[:-1]))
        y = y[-1] + y[:-1]

    if all(isP(n) for n in lis):
        primes.append(x)

print(primes)
print(len(primes))
