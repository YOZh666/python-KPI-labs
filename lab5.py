# Task 88
import sys
try:
	n = int(input("Please, enter your number: "))
except ValueError:
	print("You must enter only a number!!!")
	sys.exit()
n_2 = str(n**2)
n = str(n)
if '3' in n_2:
	print("Task A.  The square of this number contains 3")
else:
	print("Task A.  The square of this number doesn't contain 3")
lst = list(n)
lst.reverse()

print("Task B.  ", ''.join(lst))
lst.reverse()
lst[0] , lst[len(lst)-1] = lst[len(lst)-1], lst[0]
print("Task C.  ",''.join(lst))
lst[0] , lst[len(lst)-1] = lst[len(lst)-1], lst[0]
lst.append('1')
lst.insert(0,'1')
print("Task D.  ",''.join(lst))