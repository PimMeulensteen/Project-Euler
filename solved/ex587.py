#Solved!
#2240

import math
def getXofR(n):
    x = (n**2 + n)/(n**2 + 1) - math.sqrt(2) * math.sqrt(n**3/(n**2 + 1)**2)
    return x / 2

def getYofR(n):
    x = getXofR(n)
    y = (1/n) * x
    return y

def getAngleOfBAD(n):
    a = math.degrees(math.tanh(1/n))
    return a

def getLenIV(n):
    y = 0.5 -  getYofR(n)
    return y

def getLenRV(n):
    x = 0.5 - getXofR(n)
    return x

def getAngleOfIRV(n):
    ang = getLenIV(n) / getLenRV(n)
    a = math.degrees(math.atan(ang))
    return a

def getAngleOfRIV(n):
    ang = getLenRV(n) / getLenIV(n)
    a = math.degrees(math.atan( ang ))
    return a

def getLenRI(n):
    n = n + 1
    return 0.5

def getSurfaceLIR(n):
    a = getLenRV(n) * getLenIV(n)
    return a

def getSurfaceNIR(n):
    a = (math.pi * ((0.5)**2)) * (getAngleOfRIV(n)/360)
    return a

def getSurfaceNUTQ(n):
    s = getLenRV(n)
    return s


def getSurfaceNRU(n):
    s =  (getSurfaceNIR(n) * 2) + getSurfaceLIR(n)
    s = getSurfaceNUTQ(n) - s
    return s /2

def getSurfaceRUA(n):
    s = getXofR(n) * getYofR(n)

    return s / 2

def totalSufrace(n):
    return getSurfaceNRU(n) + getSurfaceRUA(n)

def percent(n):
    s = totalSufrace(n) / baseSurface
    return s * 100


baseSurface = ((0.5**2) - (0.25 * math.pi * (0.5**2)))
x = 1
while True:
    p = percent(x)
    print(x, p)
    if p < 0.1:
        print("DONE!")
        print("Answer = ", x)
        break
    x = x + 1
