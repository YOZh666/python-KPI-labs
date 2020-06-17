import random 
a = [round(random.uniform(0, 10), 2) for i in range(29)]
b = [round(random.uniform(0, 10), 2) for i in range(29)]
c = [0 for i in range(30)]
c =[round(a[29-i]/(b[29-i] - c[29-i+1]),2) for i in range(1,29)] 
c.append(0)	
print(c)