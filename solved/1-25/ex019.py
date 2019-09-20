# Solved

months = [31,28,31,30,31,30,31,31,30,31,30,31]


day = 1
counter = 0
for x in range(1901, 2001):
    for y in range(0, 12):
        day =  day + months[y]
        day = day % 7
        if day == 6:
            counter = counter + 1
print(counter)
