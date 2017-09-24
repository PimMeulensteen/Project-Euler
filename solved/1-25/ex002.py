#Solved
#4613732
fib = [1,2]
x = 1
out = 0

while True:
    fib.append(fib[x] + fib[x-1])
    x = x + 1
    if fib[x] > 4000000:
        break

for y  in range(0, len(fib)):
    if fib[y] % 2 == 0:
        out = out + fib[y]
print(fib)
print(out)
