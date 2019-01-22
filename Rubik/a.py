with open('a', 'r') as fin:
	for line in fin:
		d = line.split()
		print("dd[%s][%s] = self.d[%s][%s]" % (d[3], d[4], d[0], d[1]))