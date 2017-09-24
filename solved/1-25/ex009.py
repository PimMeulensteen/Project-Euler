biggest = 0
biggestn = 0

for x in range(2,1000):
    teller = 0
    for a in range(1, x):        
        for b in range(1, x):
            c = x - a - b
            if a * a  + b * b == c * c :
                teller = teller + 1
        
        
        
        
    if teller > biggest:
        biggestn = x
        biggest = teller
        print(biggestn)
        print(biggest)

                
                
print(biggestn)

    
