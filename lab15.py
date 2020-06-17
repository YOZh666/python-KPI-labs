import random

def main(l):
    return [i for i in l if i >=0] + [i for i in l if i < 0]

a = [round(random.uniform(-10, 10), 2) for i in range(16)]
print(a)
print(main(a))	