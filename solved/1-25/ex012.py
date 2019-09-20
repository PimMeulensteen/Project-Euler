import math
from time import time
tijd = time()
def divisors(n):
    aantal_factoren = 0
    for i in range(1, int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            aantal_factoren +=2
        else:
            continue
    return aantal_factoren

triNum =1
for y in range(2,1000000):
    triNum += y
    if divisors(triNum) >= 500:
        print(triNum)
        break

tijeind = time()-tijd
print(tijeind)