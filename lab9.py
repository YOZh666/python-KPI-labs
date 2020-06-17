import random
x = 15.34
y = [1.23]
for i in range(100):
	y.append(round(y[i]+random.uniform(0,1.25),2))
for i in range(1,100):
	if x>y[i-1] and x<y[i]:
		print("The answer k = ", i+1)
		break