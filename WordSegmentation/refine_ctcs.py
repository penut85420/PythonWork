with open('./ctcs.txt', 'r', encoding='utf-8') as fin:
	for line in fin:
		a, b = line.strip().split('\t')
		if a == b: continue
		print('%s\t%s' % (a, b))