from random import uniform
n = int(input("Input the size of your matrix: "))
a = [[round(uniform(1, 9),2) for j in range(n)] for i in range(n)]
sum = 0.0
for i in range(n):
	sum += max(a[i])*max(a[n-i-1])
print("Sum is: ", round(sum,2))
