def task_a(l):
	'''Save order of positive and negative numbers'''
	return [i for i in l if i < 0] + [i for i in l if i >= 0]
def task_b(l):
	'''Save order of positive numbers, reverse negative numbers'''
	return [i for i in l if i < 0][::-1] + [i for i in l if i >= 0] 
def task_c(l):
	'''Save order of negative numbers, reverse positive numbers'''
	return [i for i in l if i < 0] + [i for i in l if i >= 0][::-1]
def task_d(l):
	'''Reverse order of positive and negative numbers'''
	return [i for i in l if i < 0][::-1] + [i for i in l if i >= 0][::-1]
with open("TI_81_Nikishenko_lab26_f.txt") as f, open("TI_81_Nikishenko_lab26_f1.txt", 'w') as f1:
	arr = [float(x) for x in f.read().split(' ')]
	f1.write("Our sequence before operations: " + str(arr))
	f1.write("\n\nOur sequence after task A: " + str(task_a(arr)))
	f1.write("\n\nOur sequence after task B: " + str(task_b(arr)))
	f1.write("\n\nOur sequence after task C: " + str(task_c(arr)))
	f1.write("\n\nOur sequence after task D: " + str(task_d(arr)))
	
	