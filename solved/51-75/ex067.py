
pyr = []
FILE = open("p067.txt", "r")
for blob in FILE: pyr.append([int(i) for i in blob.split(" ")])


for row in range(98, -1, -1):
   print(pyr[row])
   for item in range(0, len(pyr[row])):
      pyr[row][item] +=  max(pyr[row+1][item],pyr[row+1][item+1])

print(pyr[0])
