ctcs_d = dict()

with open('./ctcs.txt', 'r', encoding='utf-8') as fin:
	for line in fin:
		try:
			t, s = line.strip().split()
			ctcs_d[t] = s
		except:
			print(line)

finn = open('./lexicon_ct.txt', 'r', encoding='utf-8')
fout = open('./lexicon_cs.txt', 'w', encoding='utf-8')

for line in finn:
	for c in line:
		fout.write(ctcs_d.get(c, c))

finn.close()
fout.close()
