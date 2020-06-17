n = 7
rng = neg = 0
arr = [12.32, 1.23, 11.23, -23, 1.43, -11, -21.22]
for i in range(n):
	if arr[i] > 0 and arr[i]<1 or arr[i]>2:
		arr[i] = 1
	elif arr[i]<0:
		neg+=1
	else:
		rng+=1
print("Negative numbers: ",neg)
print("Numbers in section [1,2]: ",rng)
print("Sequence after rework:")
print(arr)