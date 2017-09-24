#Solved 443839
sum = 0
for x in range(2,500000):
    test = 0
    y = str(x)
    for i in range(len(y)):
        test = test + (int(y[i])**5)
    if test == x:
        sum = sum + x
print(sum)
