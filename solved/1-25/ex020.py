import math
num = str(math.factorial(100))
res = 0
for x in range(0, len(num)):
    res = res + int(num[x])
print(res)
