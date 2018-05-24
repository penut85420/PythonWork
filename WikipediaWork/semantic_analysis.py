import os, re

folder_input = "zhwiki_sub_seg"
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
        for line in fin: 
            if line.startswith("<title>"):
                title = re.search("<title>(.*)</title>", line).group(1)
            if line.startswith("<preserve>"):
                log = True
                fout.write(line)
                continue
            elif line.startswith("</preserve>"):
                log = False
                content = content.replace("\n\n", "\n")
                content = content.replace("\n", " ")
                
                found_title = False
                found_is = False
                found_of = False
                tags = []
                for s in content.strip().split(" "):
                    if s == title: 
                        found_title = True
                    elif s == "是" or s == "指": 
                        found_is = True
                    elif s == "的": 
                        found_of = True
                    elif s == "。" or s == "，":
                        found_is = found_of = False
                    elif found_title and found_is and found_of:
                        tags.append(s)
                fout.write(line)
                fout.write("<tags>\n")
                for tag in tags:
                    fout.write("\t<tag>" + tag + "</tag>\n")
                fout.write("</tags>\n")
                content = ""
            
            if log: content += line
            fout.write(line)

