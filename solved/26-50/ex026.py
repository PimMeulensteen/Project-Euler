#Soved 983
import re
from decimal import *
def findR(x):
    x = str(x)
    r = re.compile(r"(.+?)\1+")
    out = r.findall(x)
    print(x)
    print(out)
    return out

biggest = 0
nr = -1
for x in range(3,1000):
    getcontext().prec = 5000
    y = Decimal(1) / Decimal(x)
    y = findR(y)
    print(y)
    for i in range(0, len(y)):
        if int(y[i]) >biggest:
            biggest = int(y[i])
            nr = x
print(biggest)
print(y[i])
print(nr)
