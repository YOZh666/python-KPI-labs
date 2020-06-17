import numpy as np
m = int(input("Please, input the size of a matrix: "))
n = int(input("Please, input your n: "))
answers_array = np.ones((m,m), dtype = np.int32)
a = np.random.randint(0, 10, (m, m))
print("Our A matrix:\n", a)
for i in range(1,n+1):
	answers_array = answers_array + a**i
print("\nOur solution:\n", answers_array)

