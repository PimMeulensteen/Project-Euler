#Solved (> 60 sec)
#1533776805

#Var declaration
triNumbers = [1]
pentNumbers = [1]
pentC = 1
hexaNumbers = [1]
hexC = 1
done = False
triC = 286

#Functions
def triF(x):
    x = (x * (x + 1)) / 2
    return x

def pentF(x):
    x = (x * (3 * x -1)) /2
    return x

def hexaF(x):
    x = (x * (2 * x-1))
    return x



#Main Code
while not done:
    print(triC)
    triNumbers.append(triF(triC))
    n = triNumbers[-1]

    while hexaNumbers[-1] < n:
        hexaNumbers.append(hexaF(hexC))
        hexC = hexC + 1
    while pentNumbers[-1] < n:
        pentNumbers.append(pentF(pentC))
        pentC = pentC + 1



    if n in hexaNumbers:
        if n in pentNumbers:
            done = True
            print(n)
    triC = triC + 1
