from math import floor;
res = 0

for num in range(2,2000000):
    print(num)
    for x in range(2, floor(num/2)):
        if num % x == 0:
            break
        elif num > x:
            res = res + num
        else:
            x = x + 1
            


print(res)
print(31875000)
