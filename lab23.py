with open("TI_81_Nikishenko_Lab23_f.txt") as f, open("TI_81_Nikishenko_Lab23_g.txt", 'w') as g: 
	g.write(f.read().lower())