import math
n = int(input("Input your n: "))
print("Answer for a: ")
n_a = 2**n
print(n_a)
n_b = math.factorial(n);
print("Answer for b: ")
print(n_b)
n_c = 1+(1/1**2)
for i in range(2,n+1):
	n_c = n_c * (1+(1/i**2))
print("Answer foc c: ")
print(n_c)

	