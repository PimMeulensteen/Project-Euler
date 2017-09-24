#Solved 9183
list = []
min = 2
max = 101
for a in range(min,max):
    for b in range(min,max):
        i = a**b
        if not i in list:
            list.append(i)
print(list)
print(len(list))
