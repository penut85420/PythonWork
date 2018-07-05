import os, re

fout = open("title_list.txt", "w", encoding="UTF-8")

for dirPath, dirName, fileNames in os.walk("zhwiki_main_tw"):
    for fileName in fileNames:        
        with open(dirPath + "\\" + fileName, "r", encoding="UTF-8") as fin:
            for line in fin:
                if re.search("<title>(.*?)</title>", line) is not None:
                    fout.write(re.search("<title>(.*?)</title>", line).group(1) + "\n")
        