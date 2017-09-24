import math
k = int(input("Enter n: "))

#Uses central binomial coefficients.
#Source http://www.robertdickau.com/lattices.html
n = 2 * k
n_k = n - k

up = math.factorial(n)
down = math.factorial(k) * math.factorial(n_k)

print(up/down)
