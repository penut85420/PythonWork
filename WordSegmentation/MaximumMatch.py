import re

class Segmentor:
	def __init__(self, lexicon_path):
		self.lexicon = dict()
		self.maxlen = 0
		self.symlist = re.compile("([A-Za-z0-9~!@#$%^&*()_+\\.,\\/]+)")
		with open(lexicon_path, 'r', encoding='utf-8') as fin:
			for line in fin:
				line = line.strip()
				self.lexicon[line] = 1
				self.maxlen = max(self.maxlen, len(line))

	def match(self, s):
		# print(s)
		m = self.symlist.match(s)
		if m: return len(m.group(1))
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
	s = "Hi. 你好！"
	print(seg.seg(s))