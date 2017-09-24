#Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
def total(a):
    a = str(a)
    out = 0
    while len(a) != 0:
        out = out + int(a[0])
        a = a[1:]
    return out

#
result = 0
for x in range(1,100):
    for y in range(1,100):
        to = total(x**y)
        if to > result:
            result = to
            
print(result)