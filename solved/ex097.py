#calculate the last 10 digits of:
#28433 x 2**7830457 + 1.
res = 2
for x in range(7830456):
    res = (res * 2) % 10000000000

    
    
res = res * 28433
res = res + 1
res = str(res)
res = res[-10:]
print(res)
#7480013585