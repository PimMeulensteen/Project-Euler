#Solved! 7654321

def isPam(nr, n):
    digits = ''.join(map(str, range(1, n + 1)))
    nr = str(nr)
    for i in digits:
        if str(i) not in nr[0:9]:
            return False
        if str(i) not in nr[-9:]:
            return False
    return True



def isprime(n):
    """Returns True if n is prime."""

    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

for x in range(7654321, 0, -2):
    #7654321 is het grootste nummer.
    #(9)87654321 voldoen niet aan deelbaarheidsregel (als je alles bij elkaar optelet is het deelbaar door 3, dus is het getal ook deelbaar door drie)
    if isPam(x, 7):
        if isprime(x):
            print(x, 'True')
            break
        else:
            print(x, "False")
