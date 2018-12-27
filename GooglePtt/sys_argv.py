import sys
import pandas as pd

flag = "-w"
word_list = []
ts = ""
file_path = "J:/"

for arg in sys.argv[1:]:
	if arg.startswith('-'): 
		flag = arg
		continue
	
	if flag == "-w":
		word_list.append(arg)
	elif flag == "-t":
		ts = pd.to_datetime(arg)
	elif flag == "-f":
		file_path = arg


print(len(word_list))
exit(0)
print(ts)
print(file_path)