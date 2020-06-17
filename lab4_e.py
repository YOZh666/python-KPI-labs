import math
n = int(input("Input n: "))
answ = math.sqrt(2)
for i in range(2,n+1):
	answ = math.sqrt(answ + 2)
print("Answer is:")
print(answ)