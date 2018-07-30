import importlib
import os
import re

StanfordParser = importlib.import_module("stanford_parser")
Lex = importlib.import_module("lex")

folder_input = "zhwiki_sub_seg_fix_small_sub"
folder_output = "zhwiki_sub_semantic"

# folder_input = "test_fin"
# folder_output = "test_fout"

for dirPath, dirName, fileNames in os.walk(folder_input):
    for fileName in fileNames:
        print(fileName)
        fin = open(dirPath + "\\" + fileName, "r", encoding="UTF-8")
        fout = open(folder_output + "\\" + fileName, "w", encoding="UTF-8")

        log = False
        content = ""
        titles = []
        for line in fin: 
            if line.startswith("<title>"):
                title = re.search("<title>(.*)</title>", line).group(1)
                titles.append(title)
            if line.startswith("<preserve>"):
                log = True
                # fout.write(line)
                continue
            elif line.startswith("</preserve>"):
                # fout.write("</preserve>\n<tagged>\n")
                # print(content)
                # content = StanfordParser.parse_string(content)
                # fout.write(str(Lex.find_title_is(content, title)))
                # fout.write("</tagged>\n")
                log = False
            
            if log: content += line
            # fout.write(line)
        
        content = StanfordParser.parse_string(content).split("\n\n")

        for i in range(len(titles)):
            fout.write("<title>" + titles[i] + "</title>\n")
            fout.write("<semantic>\n") 
            try:
                fout.write(content[i])
            except IndexError:
                None
            fout.write("\n</semantic>\n")
