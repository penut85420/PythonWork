import os

input_dir = "interlang_links_org"
output_dir = "interlang_links_zh_en\\interlangLinks_%.4d.ttl"
fid = 1
base_file_size = 4000000
zh_tag = "<http://zh.dbpedia.org/resource/"
en_tag = "<http://dbpedia.org/resource/"
zh_tag_len = len(zh_tag)
en_tag_len = len(en_tag)

def walk_dir(dirName):
	for dirPath, dirName, fileNames in os.walk(dirName):
		for fileName in fileNames:
			yield dirPath + "\\" + fileName

def walk_line(dirName):
	for fileName in walk_dir(dirName):
		fin = open(fileName, "r", encoding="UTF-8")
		for line in fin:
			yield line
		fin.close()

fout = open(output_dir % (fid), "w", encoding="UTF-8")

for line in walk_line(input_dir):
	if line.find(en_tag) != -1:
		s1 = line.find(zh_tag) + zh_tag_len
		s2 = line[s1:].find(">") + s1
		s3 = line.find(en_tag) + en_tag_len
		s4 = line[s3:].find(">") + s3
		print(s1, s2, s3, s4)
		fout.write(line[s1:s2] + "\t" + line[s3:s4] + "\n")
		if fout.tell() > base_file_size:
			fout.close()
			fid += 1
			fout = open(output_dir % (fid), "w", encoding="UTF-8")