with open("TI_81_Nikishenko_lab25_f.txt") as f, open("TI_81_Nikishenko_lab25_f1.txt", 'w') as f1:
	for line in f.readlines():
		f1.write(line.strip() + '\n')