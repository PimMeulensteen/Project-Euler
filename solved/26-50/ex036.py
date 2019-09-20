#Solved!
#872187

def intToBin(x):
    return "{0:b}".format(x)

def isPal(a):
    pal = True
    b = str(a)
    leng = len(b) -1
    for x in range(0, leng):
        if b[x] != b[leng - x]:
            pal = False
            break
    return pal
som = 0
for x in range(0,1000000):
    if isPal(x):
        if isPal(intToBin(x)):
            som = som + x
            print(x)

print(som)
