m = int(input("Please, input your m: "))
n = 1 if m>=0 else -1
n = n*int(bin(abs(m))[0:2]+bin(abs(m))[-1:1:-1],2)
print("According to the task, an appropriate number for m is:", n)