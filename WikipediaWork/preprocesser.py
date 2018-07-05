import os, re

dump_folder = "zhwiki_preserve_tw\\"
output_folder = "zhwiki_preserve_plain\\"

dump_folder = "zhwiki_sub_org"
output_folder = "zhwiki_sub_plain"

# dump_folder = "test_fin"
# output_folder = "test_fout"

replace_dict = {"&lt;": "<",
				"&quot;": "\"",
				"&gt;": ">", 
				"'''": "", 
				"''": "",
				"-{}-": "",
				"</text>": "",
				"</revision>": ""}

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
		t1 = content[:idx] # Content before tag
		t2 = content[idx + len(tag):] # Content after tagbegin
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
		print(fileName)

		fin = open(dirPath + "\\" + fileName, "r", encoding="UTF-8")
		fout = open(output_folder + "\\" + fileName, "w", encoding = "UTF-8")		

		log = False
		content = ""

		for line in fin:
			if line.startswith("<preserve>"): 
				log = True
				fout.write(line)
				continue
			elif line.startswith("</preserve>"):
				log = False
				content = re.sub("{{lang(?P<str>.*?)}}", lambda m: m.group("str")[m.group("str").rfind("|")+1:], content)
				content = re.sub("(?s)<div.*</div>", "", content)
				content = re.sub("<noinclude>.*?</noinclude>", "", content)
				def zh_hans(m):
					s = m.group(0)
					s = s[s.find("zh_hans:") + 11:]
					s = s[:s.find(";")]
					return s
				content = re.sub("-{.*?}-", zh_hans, content)
				content = re.sub("-{T.*?}-", "", content)
				content = re.sub("{{ruby-py\|(.*?)\|.*?}}", lambda m: m.group(1), content)
				content = re.sub("<sha1>.*?</sha1>", "", content)
				content = tag2_clear(content, "ref")
				content = tag_clear(content, "{{", "{", "}", 2)
				content = tag_clear(content, "{", "{", "}", 1)
				content = tag_clear(content, "[[File:", "[", "]", 2)
				content = tag_clear(content, "<!--", "<", ">", 1)
				content = re.compile("（.*?）").sub("", content)
				while content.find("[[") != -1:
					idx = content.find("[[")
					t1 = content[:idx]
					t2 = content[idx+2:]
					left = -1
					right = 2
					for i in range(len(t2)):
						if t2[i] == "|": left = i
						if t2[i] == "]": 
							right = i
							break

					t2 = t2[left+1:right] + t2[right+2:]
					content = t1 + t2
				content = content.replace("\n\n", "")
				fout.write(content.strip() + "\n")
				content = ""
			if log:
				for key in replace_dict:
					line = line.replace(key, replace_dict[key])
				if line.strip() != '':
					content += line.strip() + "\n"
			else: fout.write(line)
		fin.close()
		fout.close()

		