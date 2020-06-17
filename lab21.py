from random import randint
a = [randint(1,50) for i in range(randint(5,20))]
b = [randint(1,50) for i in range(randint(5,20))]
k = randint(1,50)
if k not in a:
	a[a.index(max(a))] = k
print(a)
if 10 not in b:
	b[b.index(max(b))] = 10
print(b)

