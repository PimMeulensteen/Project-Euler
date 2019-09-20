#Solved
primes = []
toggle = 1
xs = 1

def isPrime(x):
    global toggle
    for i in range(2, x):
        if x % i == 0:
            break
    else:
        primes.append(x)
        if len(primes) == 10001:
            toggle = 0
        print(str(x) + ' is the ' + str(len(primes)) + 's prime!')



while True:
    xs = xs + 1
    if toggle == 1:
        isPrime(xs)
    else:
        print('Done!')
        print(primes[10001])
        break
