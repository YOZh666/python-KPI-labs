#Task 115(B)
import sys
try:
	n = int(input("Please, enter an amount of members in this numerical series: "))
except ValueError:
	print("You must enter only a number!!!")
	sys.exit()
sum = 0
if n<1:
	print("This number must be more than 0")
else:
	for k in range(1, n+1):
		sum+=1/(pow((2*k+1),2))
	print("Sum of this series is: " '%.3f' % sum)

	