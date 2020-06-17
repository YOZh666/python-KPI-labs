import numpy as np
n = int(input("Please, input the size of a matrix: "))
a = np.round(np.random.uniform(-10, 10, (n, n)), decimals = 2)
a_taskB = np.round(np.random.uniform(-10, 10, (n, n)), decimals = 2)
print("TASK A MATRIX:\n ")
print(a)
#finding indexes of max
mi = np.unravel_index(np.argmin(a), a.shape)
if abs(np.max(a)) > abs(np.min(a)):
	mx = np.unravel_index(np.argmax(a), a.shape) #checking if abs(min) > max
else:
	mx = mi
#swaping rows and columns
for j in range(len(a)):
	a[0][j], a[mx[0]][j] = a[mx[0]][j], a[0][j]
for i in range(len(a)):
	a[i][0], a[i][mx[1]] = a[i][mx[1]], a[i][0]
print("\nTASK A SOLUTION:\n")
print(a)

#TASK B:
mi_b = np.unravel_index(np.argmin(a_taskB), a_taskB.shape) #indexes of min element
print("\n\nTASK B MATRIX:\n\n ")
print(a_taskB)
#swaping rows and columns
for j in range(len(a_taskB)):
	a_taskB[mi_b[0]][j], a_taskB[n-1][j], = a_taskB[n-1][j],a_taskB[mi_b[0]][j]
for i in range(len(a_taskB)):
	a_taskB[i][0], a_taskB[i][mi_b[1]] = a_taskB[i][mi_b[1]], a_taskB[i][0]
print("\nTASK B SOLUTION:\n")
print(a_taskB)
