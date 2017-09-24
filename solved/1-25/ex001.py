#Solved
#234168

out = 0
for x in range(1,1001):
    if x % 3 == 0:
        out = out + x
    elif x % 5 == 0:
        out = out + x
print(out)
