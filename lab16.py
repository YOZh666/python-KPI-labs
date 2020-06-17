a = int(input("Give me first number: "))
b = int(input("Give me second number: "))
for num in range(a,b):
    if all(num%i!=0 for i in range(2,num)):
       print(num, end = " ")