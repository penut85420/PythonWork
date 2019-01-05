
class Segmentor:
	def __init__(self, lexicon_path):
		self.lexicon = dict()
		self.maxlen = 0
		with open(lexicon_path, 'r', encoding='utf-8') as fin:
			for line in fin:
				line = line.strip()
				self.lexicon[line] = 1
				self.maxlen = max(self.maxlen, len(line))

	def match(self, s):
		# print(s)
		m = min(len(s), self.maxlen)
		for i in reversed(range(m)):
			if i == 1: return 1
			if self.lexicon.get(s[:i], None):
				return i
		return 1

	def seg(self, s):
		rtn = str()
		while len(s) > 0:
			idx = self.match(s)
			rtn += s[:idx] + ' '
			s = s[idx:]
		return rtn.strip()

if __name__ == '__main__':
	seg = Segmentor('./lexicon_ct.txt')
	s = "皇后在後面吃麵"

	print(seg.seg(s))