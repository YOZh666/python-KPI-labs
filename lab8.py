print("x\t\t\tp1(x)\t\t\tp2(x)\t\t\tp3(x)")
x = 0.0
while x <= 20.00:
	print('%.2f' % x, "\t\t\t" '%.2f' % x, "\t\t\t" '%.2f' % ((3*x**2-1)/2), "\t\t\t" '%.2f' % ((5*x**2 - 3*x)/2))
	x+=0.05
	x = round(x, 2)





