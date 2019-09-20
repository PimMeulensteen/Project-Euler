# Longest Collatz Sequence under 1.000.000
# 837799 with 525 steps


leadRes = 0
leadInp = 0

def collatz(x):
    authentic = x
    global leadRes
    global leadInp
    steps = 1
    while x != 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = (x*3)+1
        steps = steps + 1
    if steps > leadRes:
        leadRes = steps
        leadInp = authentic




x = 1
while x < 1000000:
    collatz(x)
    print('tested: ' + str(x))
    x += 1

print(leadInp)
print(leadRes)
