def Collatz_conjecture(n,gap):
	'''Hayes' sequence alghorithm'''
	for i in range(gap):
		n = n/2 if n%2 == 0 else n * 3 +1
		if n == 1:
			return True
			break
	return False

k,l,m = int(input("Please enter your k: ")), int(input("Please, enter your l: ")), int(input("Please, enter your m: "))
for i in range(k, l+1):
	if not Collatz_conjecture(i, m):
		print("This sequence is incorrect for this condition!")
		quit() #jupyter can't understand my quit() func, another solution can be with sys.exit() func
print("This sequence is correct for this condition!")		