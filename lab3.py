a = input("Input a: ")
b = input("Input b: ")
c = input("Input c: ")
x = input("Input x: ")
y = input("Input y: ")

if(a <= x and b <= y):
	print("Will pass!")
elif(a<=x and c<=y):
	print("Will pass!")
elif(b<=x and c<=y):
	print("Will pass!")
elif(a<=y and b<=x):
	print("Will pass!")
elif(a<=y and c<=x):
	print("Will pass!")
elif(b<=y and c<=x):
	print("Will pass!")
else:
	print("Will not pass!")	