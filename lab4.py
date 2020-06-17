# Task 813
text = str(input("Please, enter your text:  "))
arr = text.split(" ")
print("So, after reworking this text looks like: ")
for i in range(len(arr)):
	if not arr[i][0].isalpha() or arr[i][0].isupper():
		print(arr[i], end= ' ')
	elif arr[i].isalpha():
		print(arr[i], end = ' ')
	else:
		for j in range(10):
			arr[i] = arr[i].replace(str(j), '*')
		print(arr[i], end = ' ')