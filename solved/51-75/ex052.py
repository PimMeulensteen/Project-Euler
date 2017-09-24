#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
#same about of numebrs, so: first number of x < 10/6.
import time
start_time = time.time()
def num(x):
    x = list(str(x))
    x.sort()
    return x
    

x = 1
while True:
    n1 = num(x)
    n2 = num(x * 2)
    if n1 == n2:
        n3 = num(x * 3)
        if n1 == n3:
            n4 = num(x * 4)
            if n1 == n4:
                n5 = num(x * 5)
                if n1 == n5:
                    n6 = num(x * 6)
                    if n1 == n6:
                        print(x)
                        print('done!')
                        break
                    else:
                        x = x + 1
                else:
                    x = x + 1
            else:
                x = x + 1
        else:
            x = x + 1
    else:
        x = x + 1
          
print("%s seconds" % (time.time() - start_time))  