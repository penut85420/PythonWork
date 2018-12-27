import sys
import re
import pyperclip as pc

copy_dict = {}

with open("Copy.txt", "r", encoding="UTF-8") as fin:
	for line in fin:
		ss = re.sub("[\ufeff\r\n]", "", line).split("\t")
		copy_dict[ss[0].lower()] = ss[1]

if len(sys.argv) < 2:
	for k in copy_dict.keys():
		print(k.title().ljust(15) + "\t" + copy_dict[k])
else:
	for k in copy_dict.keys():
		if k.find(sys.argv[1].lower()) >= 0:
			pc.copy(copy_dict[k])
			print(copy_dict[k] + " has been copied.")
			break
