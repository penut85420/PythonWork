import os

dump_folder = "zhwiki_preserve_tw"
output_folder = "zhwiki_preserve_plain"

# dump_folder = "zhwiki_sub_pre"
# output_folder = "zhwiki_sub_plain"

replace_dict = {"&lt;": "<",
				"&quot;": "\"",
				"&gt;": ">", 
				"'''": "", 
				"''": ""}

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

def template_bd(txt):
    tag = "{{bd|"
    p = txt.find(tag)

    if p < 0: return txt
    
    t1 = txt[:p]
    t2 = txt[p + len(tag):]
    t3 = t2[t2.find("}}") + 2:]
    t2 = t2[:t2.find("}}")]

    arg = t2.split("|")

    t2 = arg[0] + arg[1] + "－"

    for a in arg[1:-1]:
        t2 += a
    return template_bd(t1 + t2 + t3)

for dirPath, dirName, fileNames in os.walk(dump_folder):
	for fileName in fileNames:
		content = ""
		with open(dirPath + "\\" + fileName, "r", encoding="UTF-8") as fin:
			print(fileName)
			for line in fin:
				s = line
				for key in replace_dict:
					s = s.replace(key, replace_dict[key])
				if s.strip() != '':
					content += s.strip() + "\n"

		content = tag2_clear(content, "ref")
		content = tag2_clear(content, "div")

		# content = template_bd(content)
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

		with open(output_folder + "\\" + fileName, "w", encoding = "UTF-8") as fout:
			fout.write(content.strip())