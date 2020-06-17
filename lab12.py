import random
a = [random.randint(0,100) for i in range(10)]
print(a)
if a[0]<a[1]:
	for i, (x, y) in enumerate(zip(a, a[1::])):
		if x>y:
			print(a[0:i+1])
			break
else:
	for i, (x, y) in enumerate(zip(a, a[1::])):
		if x<y:
			print(a[0:i+1])
			break