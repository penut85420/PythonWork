class Surface:
	def __init__(self, c):
		self.d = [
			#0  1  2
			[c, c, c], # 0
			[c, c, c], # 1
			[c, c, c], # 2
		]
		self.get = {
			'col': self.getCol,
			'row': self.getRow,
		}
		self.put = {
			'col': self.putCol,
			'row': self.putRow,
		}
	
	def rotate(self):
		"""
		0 0 > 0 2
		0 2 > 2 2
		2 2 > 2 0
		2 0 > 0 0
		0 1 > 1 2
		1 2 > 2 1
		2 1 > 1 0
		1 0 > 0 1
		"""
		dd = [[0, 0, 0],[0, self.d[1][1], 0],[0, 0, 0]]
		dd[0][2] = self.d[0][0]
		dd[2][2] = self.d[0][2]
		dd[2][0] = self.d[2][2]
		dd[0][0] = self.d[2][0]
		dd[1][2] = self.d[0][1]
		dd[2][1] = self.d[1][2]
		dd[1][0] = self.d[2][1]
		dd[0][1] = self.d[1][0]
		self.d = dd
	
	def getCol(self, n):
		return [self.d[i][n] for i in range(3)]
	
	def getRow(self, n):
		return [self.d[n][i] for i in range(3)]
	
	def putCol(self, n, r):
		for i in range(3):
			self.d[i][n] = r[i]

	def putRow(self, n, r):
		for i in range(3):
			self.d[n][i] = r[i]

	def __str__(self):
		s = str()
		for i in self.d:
			for j in i:
				s += j
			s += '\n'
		return s

class Cube:
	def __init__(self):
		d = [
			["UDFBRL"],
			["WYGBRO"]
		]
		self.sur_info = dict([(d[0][0][i], d[1][0][i]) for i, _ in enumerate(d[0][0])])
		self.sur = dict()
		for key in self.sur_info.keys():
			self.sur[key] = Surface(self.sur_info[key])
		self.do = {
			'R': ("UFDB", "BUFD", "R", "col", 2),
			'L': ("UFDB", "FDBU", "L", "col", 0),
			'U': ("FLBR", "LBRF", "U", "row", 0),
			'D': ("FLBR", "RFLB", "D", "row", 2),
			# R2 C0 R0 C2
			'F': ("ULDR", "RULD", "F", 'row', 2),
			# R0 C0 
			'B': ("ULDR", "LDRU", "B", 'row', 0),
		}

	def __str__(self):
		s = str()
		for k in self.sur.keys():
			s += "[%s Surface]\n" % k
			s += str(self.sur[k])
		return s
	
	def doRotate(self, src, dst, rotate, t, n):
		rr_sur = list()
		for r in src:
			rr_sur.append(self.sur[r].get[t](n))
		for i, r in enumerate(dst):
			self.sur[r].put[t](n, rr_sur[i])
		self.sur[rotate].rotate()

	def doAction(self, d):
		src, dst, r, t, n = self.do[d]
		self.doRotate(src, dst, r, t, n)

c = Cube()
c.doAction('F')
c.doAction('B')
print(c)