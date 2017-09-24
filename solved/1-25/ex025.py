#Sovled!
#4782
f = [1,1]
while True:
    f.append(f[-1]+f[-2])
    if len(str(f[-1])) >= 1000:
        print(len(f))
        break
