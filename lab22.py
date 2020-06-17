def fn(a, c, n):
	global f
	if 0 <= n <= 9:
		f = n
	else:
		g = (a*n+c)%10
		fn(a, c, n-1-g)
		f = g * f + n
a = int(input("Input your a:  "))
c = int(input("Input your c:  "))
m = int(input("Input your m:  "))
fn(a,c,m)
print("The answer is:  ", f)
