# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0 (19 digits)
# _ is any single digit.
def match(n):
    s = str(n)
    return not all(int(s[x*2]) == x+1 for x in range(9))

n = 138902663    # sqrt(19293949596979899)
while match(n * n): 
    n -= 2
    
print(n*10) #adding a zero