import math
n = int(input("Fill in n: "))
sum_sin = 0
answ = 0
for i in range(1,n+1):
	sum_sin = sum_sin + math.sin(i)
	answ = answ + 1/sum_sin
print("Answer is: ")
print(answ)