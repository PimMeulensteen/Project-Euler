#Solved
biggest = 0

def palCheck(a): #checks if a = palindrome
    global biggest
    pal = 1
    b = str(a)
    leng = len(b) -1

    for x in range(0, leng):
        if b[x] != b[leng - x]:
            pal = 0
            break

    if pal == 1:
        if a > biggest:
            biggest = a
        print(biggest)


for x in range(1, 1000):
    x = x - 1
    for y in range(1, 1000):
        y = y - 1
        a = x * y
        palCheck(a)

print(biggest)
