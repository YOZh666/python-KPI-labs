n = 9
arr = [12.32, 1.23, 11.23, -23, 1.43, -11, -21.22, 10.06, 5.23]
print("Values of variable j: ")
for i in range(1,n):
	if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
		print(i+1, end = " ")
