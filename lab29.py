import random
import itertools 
from math import sqrt

def calc_interception(t1,t2):
	'''simple variant of intercection function from SymPy '''
	x1,y1,r1 = t1[0], t1[1], t1[2]
	x2,y2,r2 = t2[0], t2[1], t2[2]
	dist = sqrt(((x2 - x1)**2 + (y2-y1)**2))
	if not dist:
		return False if r1 != r2 else True #the same circles
	else:
		return False if dist > r1+r2 else True #return True if intersect

def unique(t1,t2):
	'''function for task b, check if one circle is in another '''
	x1,y1,r1 = t1[0], t1[1], t1[2]
	x2,y2,r2 = t2[0], t2[1], t2[2]
	dist = sqrt(((x2 - x1)**2 + (y2-y1)**2))
	return False if dist < abs(r1-r2) else True
	
	
n = int(input("Please, input an amount of circles: "))

#fill at random, than make new list of tuples to work with individual circle easier 
coord = [random.randint(1,10) if i%3 == 0  else random.randint(-10,10) for i in range(1,n*3+1) ] #radius must be > 0, so check every 3-rd element
coord = [tuple(coord[i:i+3]) for i in range(0, len(coord), 3)]
print("Our circles: ")
print(coord)

#task b
print("Secluded circles:")
for i in range(n):
	tmp = coord[0:i] + coord[i+1:] #we cant't compare circle with itself
	#check all another circles
	if all(not calc_interception(coord[i], tmp[j]) and unique(coord[i], tmp[j]) for j in range(n-1)):
		print(coord[i])
			
#task a
combinations = list(itertools.combinations([i for i in range(n)], 3)) #all possible combinations without repeated combinations
for x,y,z in combinations:
	if calc_interception(coord[x], coord[y]) and calc_interception(coord[x], coord[z]) and calc_interception(coord[y], coord[z]): #if all intersect
		print("This sequence has got 3 pairwise intersecting circles, as follows:")
		print(coord[x], coord[y], coord[z]) 
		break #stop checking after positive result
else: 
	print("This sequence has not got 3 pairwise intersecting circles!")
