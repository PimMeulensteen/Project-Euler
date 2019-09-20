#Solved
def d(x):
    sum = 0
    for y in range(1, x):
        if x % y == 0:
            sum = sum + y
    return sum

amicables = []
for a in range(0,10000):
    da = d(a)
    if d(da) == a and a != d(a):
        amicables.append(a)


print(amicables)
print(sum(amicables))
