import string
with open("TI_81_Nikishenko_lab24_f1.txt") as f1, open("TI_81_Nikishenko_lab24_f2.txt") as f2:
	txt = f1.read()
	replace = f2.read().split(',')
replace = list(zip(replace[0::2], replace[1::2]))
for a,b in replace:
	if a in txt:
		txt = txt.replace(a, b)
with open("TI_81_Nikishenko_lab24_g.txt", 'w') as g:
	g.write(txt) 