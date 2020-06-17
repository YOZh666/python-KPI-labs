from random import uniform
a = [[round(uniform(1, 9),1) if i > j else 0.0 for j in range(12)] for i in range(12)]
for i in a: print(i)