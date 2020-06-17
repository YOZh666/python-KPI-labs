import math
k = int(input("Input your k: "))
a = float(input("Input your a: "))
x_prev = a
x = ((k-1)/k * x_prev) + (a/(x_prev**(k-1)))
while math.fabs(x**k - a) < 10**(-4):
	x_prev = x
	x = ((k-1)/k * x_prev) + (a/(x_prev**(k-1)))
print("The answer is: ", round(x, 2))	