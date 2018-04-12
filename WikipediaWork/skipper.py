import os

input_dir = "zhwiki_sub_org"
output_dir = "zhwiki_sub_plain\\"
flog = open("log.log", "w", encoding="UTF-8")

for dirPath, dirName, fileNames in os.walk(input_dir):
	for fileName in fileNames:
		print(fileName)
		fin = open(dirPath + "\\" + fileName, "r", encoding="UTF-8")
		fout = open(output_dir + fileName, "w", encoding="UTF-8")
		
		record = True
		left = 0
		
		for line in fin:
			if line == "\n": continue
			line_len = len(line)
			i = 0
			tell = fout.tell()
			while i < line_len:
				
				if left == 0: record = True

				if line[i:i+2] == "{{":
					record = False
					left = 1
				elif line[i] == "{":
					left += 1
				elif line[i] == "}":
					left -= 1
				elif line[i] == "\n":
					record = False
				if record: 
					flog.write("[" + line[i] + "]\n")
					fout.write(line[i])
				i += 1
			if tell != fout.tell():
				fout.write("\n")
		fin.close()
		fout.close()