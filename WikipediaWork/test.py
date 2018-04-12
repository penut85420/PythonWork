import os
import time

def tag_clear(content, tagTrigger, tagLeft, tagRight, d_left):
	while content.find(tagTrigger) != -1:
		idx = content.find(tagTrigger)
		t1 = content[:idx]
		t2 = content[idx + d_left:]
		left = d_left
		for i in range(len(t2)):
			if t2[i] == tagLeft: left += 1
			elif t2[i] == tagRight: left -= 1
			if left <= 0:
				left = i
				break
		t2 = t2[left + 1:]
		content = t1 + t2
	return content

def tag2_clear(content, tagName):
	# TODO: 巢狀Tag
	tag = "<" + tagName
	tagEnd = "</" + tagName + ">"

	while content.find(tag) != -1:
		idx = content.find(tag)
		t1 = content[:idx]
		t2 = content[idx + len(tag):]
		isSelfClose = False
		for i in range(len(t2)):
			if t2[i] == ">": break
			elif t2[i] == "/":
				isSelfClose = True
		if isSelfClose: idx = t2.find("/>") + 2
		else: idx = t2.find(tagEnd) + len(tagEnd)
		t2 = t2[idx:]
		content = t1 + t2
	return content

# dump_folder = "zhwiki_preserve_tw"
# output_folder = "zhwiki_preserve_plain\\"
dump_folder = r"D:\Research\Wikipedia\zhwiki_preserve_tw"
output_folder = r"D:\Research\Wikipedia\zhwiki_preserve_plain" + "\\"

replace_dict = {"&lt;": "<",
				"&quot;": "\"",
				"&gt;": ">", 
				"'''": "", 
				"''": ""}

for dirPath, dirNames, fileNames in os.walk(dump_folder):
	for fileName in fileNames:
		fin = open(dirPath + "\\" + fileName, "r", encoding="UTF-8")
		fout = open(output_folder + fileName, "w", encoding="UTF-8")
		print(fileName)
		content = ""
		record = False
		for line in fin:
			if line == "\n": continue
			for key in replace_dict:
					line = line.replace(key, replace_dict[key])

			if line.startswith("<preserve>"):
				record = True
			elif line.startswith("</preserve>"):
				record = False

				content = tag2_clear(content, "ref")
				content = tag2_clear(content, "div")
				content = tag_clear(content, "{{", "{", "}", 2)
				content = tag_clear(content, "[[File:", "[", "]", 2)
				content = tag_clear(content, "<!--", "<", ">", 1)
				
				while content.find("[[") != -1:
					idx = content.find("[[")
					t1 = content[:idx]
					t2 = content[idx + 2:]
					left = -1
					right = 2
					for i in range(len(t2)):
						if t2[i] == "|": left = i
						if t2[i] == "]": 
							right = i
							break
					t2 = t2[left+1:right] + t2[right+2:]
					content = t1 + t2
				fout.write(content.strip() + "\n")
				content = ""
			elif record:
				content += line
				continue
			fout.write(line)