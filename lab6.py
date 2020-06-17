# Task 105
import sys
try:
	n = int(input("Please enter n variable: "))
	x = float(input("Please enter x variable: "))
except ValueError:
	print("You must enter only a number!!!")
	sys.exit()
print("Task A.   ", '%.3f' % (pow(x, n**2)/pow(2, n)))
print("Task B.   ", '%.3f' % (pow(x, n**3)/pow(3, n)))