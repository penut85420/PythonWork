import re

class Node:
	def __init__(self, token, isEnd = True):
		self.mToken = token
		self.mIsEnd = isEnd
		self.mChild = {}
	
	def add(self, token):
		if (len(token) <= 0): return 

		if (len(token) == 1):
			self.mChild[token] = Node(token)
			return 

		first = token[0]
		if (self.mChild.get(first) == None):
			self.mChild[first] = Node(token, False)
		self.mChild[first].add(token[1:])

	def match(self, s, last_complete, last_longest):
		if len(s) == 1:
			if self.mIsEnd: 
				last_complete = last_longest
				return last_complete
		
		second = s[1]

		if self.mIsEnd: last_complete = last_longest

		if self.mChild.get(second) == None:
			return last_complete
		
		last_longest += second

		return self.mChild[second].match(s[1:], last_complete, last_longest)

	def __str__(self):
		s = " " + self.mToken + " " + str(self.mIsEnd)
		for n in self.mChild:
			s += "\n" + str(n)
		return s

	def print(self):
		s = " " + self.mToken + " " + str(self.mIsEnd)
		for n in self.mChild:
			s += "\n" + str(n)
		return s

class Dictionary:
	def __init__(self, dict_path):
		self.mDict = {}
		for path in dict_path:
			with open(path, "r", encoding="UTF-8") as fin:
				for line in fin:
					self.add(line.strip())
	
	def add(self, token):
		if len(token) < 1: return
		if len(token) == 1 and self.mDict.get(token) == None:
			self.mDict[token] = Node(token)
			return

		first = token[0]
		if (self.mDict.get(first) == None):
			self.mDict[first] = Node(first, False)
		self.mDict[first].add(token[1:])

	def match(self, s):
		first = s[0]
		n = self.mDict.get(first)
		if n == None: return first
		return n.match(s, first, first)

	def __str__(self):
		s = ""
		for key in self.mDict.keys():
			s += key + " {\n"
			s += self.mDict[key].print()
			s += "\n}\n\n"
		return s
	
	def __test__(self):
		print(str(self.mDict))

class CharacterList:
	def __init__(self, path):
		self.mList = {}
		with open(path, "r", encoding="UTF-8") as fin:
			for line in fin:
				for i in range(len(line)):
					self.mList[line[i]] = True
	
	def is_in_list(self, s):
		for c in s:
			if self.mList.get(c) == None:
				return False
		return True
	
	def match_list(self, s):
		i = 1
		flag = True
		while i < len(s):
			if not self.is_in_list(s[:i]):
				break
			i += 1
			flag = False
		if flag: return None
		return s[:i]

class WordSegmentor:
	def __init__(self):
		dict_path = ["dictionary_user.txt", "dictionary_main.txt"]
		self.mDict = Dictionary(dict_path)
		self.mList = CharacterList("list_alphabet.txt")

	def MaximumMatch(self, fin, fout):
			if self.mDict == None:
				print("Dictionary not initialize.")
				return 
			
			with open(fout, "w", encoding="UTF-8") as fout:
				for line in open(fin, "r", encoding="UTF-8").readlines():
					i = 0
					while i < len(line):
						s = line[i:]

						if s[0] == " ":
							i += 1
							continue

						alphabet = self.mList.match_list(s)
						if alphabet is not None:
							i += len(alphabet)
							fout.write(alphabet + " ")
							continue

						match = self.mDict.match(s)
						i += len(match)
						fout.write(match)
						
						if re.compile("[。！？!?]").search(match):
							fout.write("\r\n")
						elif re.compile("[，；：,:;]").search(match):
							fout.write("  ")
						elif re.compile("[\r\n]").search(match):
							pass
						else: fout.write(" ")
	
	def maximum_match(self, line):
		r = ""
		i = 0
		while i < len(line):
			s = line[i:]

			if s[0] == " ":
				i += 1
				continue

			alphabet = self.mList.match_list(s)
			if alphabet is not None:
				i += len(alphabet)
				r += alphabet + " "
				continue

			match = self.mDict.match(s)
			i += len(match)
			r += match
			
			if re.compile("[。！？!?]").search(match):
				r += "\r\n"
			elif re.compile("[，；：,:;]").search(match):
				r += "  "
			elif re.compile("[\r\n]").search(match):
				pass
			else: r += " "
		return r
import os

w = WordSegmentor()
print("Build Dict")
input_dir = r"E:\Document\Programming\Python\PythonWork\WikipediaWork\zhwiki_sub_plain_preprocess"
seg_dir = r"E:\Document\Programming\Python\PythonWork\WikipediaWork\zhwiki_sub_seg\\"

for dirPath, dirNames, fileNames in os.walk(input_dir):
	for fileName in fileNames:
		print(fileName)
		fin = open(input_dir + "\\" + fileName, "r", encoding="UTF-8")
		fout = open(seg_dir + fileName, "w", encoding="UTF-8")
		log = False
		content = ""
		for line in fin:
			if line.startswith("<preserve>"):
				log = True
				fout.write(line)
				continue
			if line.startswith("</preserve>"):
				log = False
				fout.write(w.maximum_match(content).split("\r\n")[0])
				content = ""

			if log:
				content += line
			else:
				fout.write(line)