from random import random
a = [[chr(int(random() * (ord('z')-ord('a'))) +ord('a')) if i > j else 'a' for j in range(10)] for i in range(10)]
for i in a: print(i)