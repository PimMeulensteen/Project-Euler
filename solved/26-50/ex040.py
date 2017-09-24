#Champernowne's constant
#All positive numers written in series (0.1 2 3 4 5 6...)
#If d(n) represents the (n)th digit of the fractional part, find the value of the following expression.
#d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
#Solved! 210

num = '0'
counter = 1
while len(num) < 1000001:
    num = num + str(counter)
    counter = counter + 1


result = int(num[1]) *  int(num[10]) *  int(num[100]) *  int(num[1000]) *  int(num[10000]) * int( num[100000]) * int( num[1000000] )

print(result)
